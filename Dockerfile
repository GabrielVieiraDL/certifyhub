FROM mcr.microsoft.com/dotnet/sdk:10.0 AS build
WORKDIR /src

COPY ["src/CertifyHub.Domain/CertifyHub.Domain.csproj", "src/CertifyHub.Domain/"]
COPY ["src/CertifyHub.Infrastructure/CertifyHub.Infrastructure.csproj", "src/CertifyHub.Infrastructure/"]
COPY ["src/CertifyHub.Api/CertifyHub.Api.csproj", "src/CertifyHub.Api/"]
COPY ["src/CertifyHub.Web/CertifyHub.Web.csproj", "src/CertifyHub.Web/"]

RUN dotnet restore "src/CertifyHub.Web/CertifyHub.Web.csproj"

COPY . .
WORKDIR "/src/src/CertifyHub.Web"
RUN dotnet publish "CertifyHub.Web.csproj" -c Release -o /app/publish /p:UseAppHost=false

FROM mcr.microsoft.com/dotnet/aspnet:10.0 AS final
WORKDIR /app
COPY --from=build /app/publish .

ENV ASPNETCORE_URLS=http://+:8080
ENV ASPNETCORE_ENVIRONMENT=Production
ENV ApiBaseUrl=http://127.0.0.1:8080
EXPOSE 8080

ENTRYPOINT ["dotnet", "CertifyHub.Web.dll"]
