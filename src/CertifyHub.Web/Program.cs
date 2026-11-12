using CertifyHub.Api.Endpoints;
using CertifyHub.Infrastructure.Data;
using CertifyHub.Web.Components;
using CertifyHub.Web.Services;
using Microsoft.EntityFrameworkCore;
using Microsoft.FluentUI.AspNetCore.Components;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddRazorComponents()
    .AddInteractiveServerComponents();

builder.Services.AddFluentUIComponents(options =>
{
    options.UseGlobalOverlay = false;
});

// Configuração do SQLite e DbContext
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection") 
    ?? "Data Source=certifyhub.db";

builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlite(connectionString));

// CORS
builder.Services.AddCors(options =>
{
    options.AddDefaultPolicy(policy =>
    {
        policy.AllowAnyOrigin()
              .AllowAnyHeader()
              .AllowAnyMethod();
    });
});

var apiBaseUrl = builder.Configuration["ApiBaseUrl"] ?? "http://127.0.0.1:8080";
builder.Services.AddHttpClient<ExamApiService>(client =>
{
    client.BaseAddress = new Uri(apiBaseUrl);
});

var app = builder.Build();

app.UseCors();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error", createScopeForErrors: true);
    app.UseHsts();
}
app.UseStatusCodePagesWithReExecute("/not-found", createScopeForStatusCodePages: true);

app.UseAntiforgery();

app.MapStaticAssets();
app.MapRazorComponents<App>()
    .AddInteractiveServerRenderMode();

// Endpoints da API REST
app.MapExamEndpoints();
app.MapSessionEndpoints();

// Inicialização e Seed do banco SQLite caso ainda não exista
using (var scope = app.Services.CreateScope())
{
    var db = scope.ServiceProvider.GetRequiredService<AppDbContext>();
    await SeedData.InitializeAsync(db);
}

app.Run();
