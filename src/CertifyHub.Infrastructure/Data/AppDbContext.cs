using CertifyHub.Domain.Entities;
using CertifyHub.Domain.Enums;
using Microsoft.EntityFrameworkCore;

namespace CertifyHub.Infrastructure.Data;

public class AppDbContext(DbContextOptions<AppDbContext> options) : DbContext(options)
{
    public DbSet<Exam> Exams => Set<Exam>();
    public DbSet<SkillDomain> SkillDomains => Set<SkillDomain>();
    public DbSet<Question> Questions => Set<Question>();
    public DbSet<Option> Options => Set<Option>();
    public DbSet<ExamSession> ExamSessions => Set<ExamSession>();
    public DbSet<UserAnswer> UserAnswers => Set<UserAnswer>();

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        base.OnModelCreating(modelBuilder);

        // Exam
        modelBuilder.Entity<Exam>(entity =>
        {
            entity.HasKey(e => e.Id);
            entity.Property(e => e.Code).IsRequired().HasMaxLength(20);
            entity.Property(e => e.Name).IsRequired().HasMaxLength(200);

            entity.HasMany(e => e.Domains)
                  .WithOne(d => d.Exam)
                  .HasForeignKey(d => d.ExamId)
                  .OnDelete(DeleteBehavior.Cascade);
        });

        // SkillDomain
        modelBuilder.Entity<SkillDomain>(entity =>
        {
            entity.HasKey(d => d.Id);
            entity.Property(d => d.Name).IsRequired().HasMaxLength(200);

            entity.HasMany(d => d.Questions)
                  .WithOne(q => q.Domain)
                  .HasForeignKey(q => q.DomainId)
                  .OnDelete(DeleteBehavior.Cascade);
        });

        // Question
        modelBuilder.Entity<Question>(entity =>
        {
            entity.HasKey(q => q.Id);
            entity.Property(q => q.Statement).IsRequired();
            entity.Property(q => q.Explanation).IsRequired();
            entity.Property(q => q.Type).HasConversion<string>();

            entity.HasMany(q => q.Options)
                  .WithOne(o => o.Question)
                  .HasForeignKey(o => o.QuestionId)
                  .OnDelete(DeleteBehavior.Cascade);
        });

        // Option
        modelBuilder.Entity<Option>(entity =>
        {
            entity.HasKey(o => o.Id);
            entity.Property(o => o.Letter).IsRequired().HasMaxLength(5);
            entity.Property(o => o.Text).IsRequired();
        });

        // ExamSession
        modelBuilder.Entity<ExamSession>(entity =>
        {
            entity.HasKey(s => s.Id);
            entity.Property(s => s.Mode).HasConversion<string>();
            entity.Property(s => s.Status).HasConversion<string>();

            entity.HasOne(s => s.Exam)
                  .WithMany()
                  .HasForeignKey(s => s.ExamId)
                  .OnDelete(DeleteBehavior.Restrict);

            entity.HasMany(s => s.Answers)
                  .WithOne(a => a.Session)
                  .HasForeignKey(a => a.SessionId)
                  .OnDelete(DeleteBehavior.Cascade);
        });

        // UserAnswer
        modelBuilder.Entity<UserAnswer>(entity =>
        {
            entity.HasKey(a => a.Id);
            entity.Property(a => a.SelectedOptionIds).IsRequired().HasMaxLength(500);

            entity.HasOne(a => a.Question)
                  .WithMany()
                  .HasForeignKey(a => a.QuestionId)
                  .OnDelete(DeleteBehavior.Restrict);
        });
    }
}
