# 📚 Modular Prompt Architecture Library

Welcome to the **Modular Prompt Repository**. This collection provides 42 battle-tested, high-precision system prompts categorized into modular domain hierarchies: **Android Engineering**, **General Software Engineering**, and **Dark Fantasy RPG Worldbuilding**.

Each prompt is designed to act as an autonomous agentic persona with strict `<system_instructions>`, workflow constraints, and deterministic `<output_format>` requirements.

---

## 🗂️ Directory Taxonomy

```
shed-prompts/
├── 📱 android/                        # Android Mobile Engineering Domain
│   ├── README.md                   # Category overview & pipeline guide
│   ├── architecture-refactoring/   # Lifecycle & breaking migrations
│   │   ├── android-architecture.md
│   │   └── android-migration.md
│   ├── ops-performance/            # Telemetry, build releases, i18n & perf
│   │   ├── android-dependency.md
│   │   ├── android-i18n.md
│   │   ├── android-observability.md
│   │   ├── android-performance.md
│   │   └── android-release.md
│   └── quality-security/           # Security, permissions, WCAG & testing
│       ├── android-a11y.md
│       ├── android-audit.md
│       ├── android-permissions.md
│       ├── android-security.md
│       └── android-testing.md
│
├── 💻 software-engineering/           # General Software & System Engineering Domain
│   ├── README.md                   # Category overview & pipeline guide
│   ├── architecture/               # Refactoring, modularization & DB schemas
│   │   ├── migration.md
│   │   ├── modularize.md
│   │   └── schema.md
│   ├── ops-performance/            # Incident postmortems, telemetry, bundling & perf
│   │   ├── bundle.md
│   │   ├── changelog.md
│   │   ├── i18n.md
│   │   ├── observability.md
│   │   ├── performance.md
│   │   ├── postmortem.md
│   │   └── testing.md
│   ├── product-strategy/           # Ideation, scaffolding & feature engineering
│   │   ├── feature.md
│   │   ├── ideation.md
│   │   ├── improvement.md
│   │   └── onboarding.md
│   └── quality-security/           # Code quality audits, AppSec & PR reviews
│       ├── a11y.md
│       ├── audit-implementation.md
│       ├── audit.md
│       ├── dependency.md
│       ├── review.md
│       └── security.md
│
└── ⚔️ worldbuilding/                  # Dark Medieval Fantasy RPG Worldbuilding
    ├── README.md                   # Category overview & lore pipeline
    ├── entities/                   # Bestiary entries & character dossiers
    │   ├── bestiary.md
    │   └── character.md
    ├── factions-beliefs/           # Lineages, factions, pantheons & faiths
    │   ├── bloodline.md
    │   ├── faction.md
    │   ├── pantheon.md
    │   └── religion.md
    └── lore-systems/               # Relics, historical events, places & magic
        ├── artifact.md
        ├── event.md
        ├── location.md
        └── magic.md
```

---

## 📑 Master Catalog

### 📱 Android Mobile Engineering (12 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `android-a11y` | [`android/quality-security/android-a11y.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-a11y.md) | `ANDROID_A11Y.md` | WCAG 2.1 AA TalkBack / Switch Access compliance audit & fix. |
| `android-architecture` | [`android/architecture-refactoring/android-architecture.md`](file:///home/sysadmin/Downloads/shed-prompts/android/architecture-refactoring/android-architecture.md) | `ANDROID_ARCHITECTURE.md` | Process death & state persistence architecture design. |
| `android-audit` | [`android/quality-security/android-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-audit.md) | `ANDROID_AUDIT.md` | Read-only code quality & memory leak risk audit. |
| `android-dependency` | [`android/ops-performance/android-dependency.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-dependency.md) | `ANDROID_DEPENDENCY_REPORT.md` | Gradle dependency & version catalog security updates. |
| `android-i18n` | [`android/ops-performance/android-i18n.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-i18n.md) | `ANDROID_I18N.md` | Multi-locale string extraction and RTL layout support. |
| `android-migration` | [`android/architecture-refactoring/android-migration.md`](file:///home/sysadmin/Downloads/shed-prompts/android/architecture-refactoring/android-migration.md) | `ANDROID_MIGRATION.md` | Target SDK bump, View→Compose, and breaking API migration. |
| `android-observability` | [`android/ops-performance/android-observability.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-observability.md) | `ANDROID_OBSERVABILITY.md` | Crashlytics, Sentry, ANR, and structured log instrumentation. |
| `android-performance` | [`android/ops-performance/android-performance.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-performance.md) | `ANDROID_PERFORMANCE.md` | Profiling-driven optimization for frames, memory & cold start. |
| `android-permissions` | [`android/quality-security/android-permissions.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-permissions.md) | `ANDROID_PERMISSIONS.md` | Least-privilege runtime permission and privacy audit. |
| `android-release` | [`android/ops-performance/android-release.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-release.md) | `ANDROID_RELEASE.md` | Play Store signed AAB/APK release packaging pipeline. |
| `android-security` | [`android/quality-security/android-security.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-security.md) | `ANDROID_SECURITY.md` | APK security audit, keystore protection, and vulnerability fix. |
| `android-testing` | [`android/quality-security/android-testing.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-testing.md) | `ANDROID_TESTING.md` | Unit, instrumented, and Compose UI test suite pass. |

---

### 💻 Software & System Engineering (20 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `a11y` | [`software-engineering/quality-security/a11y.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/a11y.md) | `A11Y.md` | WCAG 2.1 AA accessibility audit and UI remediation. |
| `audit-implementation` | [`software-engineering/quality-security/audit-implementation.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/audit-implementation.md) | Code Fixes | Executing actionable code fixes from audit recommendations. |
| `audit` | [`software-engineering/quality-security/audit.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/audit.md) | `AUDIT.md` | Read-only code quality & architecture flaw audit. |
| `bundle` | [`software-engineering/ops-performance/bundle.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/bundle.md) | `BUNDLE_REPORT.md` | Production web bundle optimization & static distribution. |
| `changelog` | [`software-engineering/ops-performance/changelog.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/changelog.md) | `CHANGELOG.md` | Prepending Keep-a-Changelog user release notes. |
| `dependency` | [`software-engineering/quality-security/dependency.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/dependency.md) | Code Updates | Security dependency updates and CVE patch pass. |
| `feature` | [`software-engineering/product-strategy/feature.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/product-strategy/feature.md) | Feature Code | Autonomous end-to-end feature implementation pass. |
| `i18n` | [`software-engineering/ops-performance/i18n.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/i18n.md) | `I18N.md` | Multi-locale string extraction and translation readiness. |
| `ideation` | [`software-engineering/product-strategy/ideation.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/product-strategy/ideation.md) | `IDEA_BUNDLE.md` | Greenfield or extension app portfolio ideation and scoring. |
| `improvement` | [`software-engineering/product-strategy/improvement.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/product-strategy/improvement.md) | Code Fixes | Proactive code quality & developer experience pass. |
| `migration` | [`software-engineering/architecture/migration.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/architecture/migration.md) | `MIGRATION.md` | Framework/runtime major version breaking change migration. |
| `modularize` | [`software-engineering/architecture/modularize.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/architecture/modularize.md) | `MODULARIZE.md` | Monolith decomposition into clean decoupled modules. |
| `observability` | [`software-engineering/ops-performance/observability.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/observability.md) | `OBSERVABILITY.md` | OpenTelemetry logging, metrics, and tracing instrumentation. |
| `onboarding` | [`software-engineering/product-strategy/onboarding.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/product-strategy/onboarding.md) | `ONBOARDING.md` | Creating repository setup guides & architectural docs. |
| `performance` | [`software-engineering/ops-performance/performance.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/performance.md) | `PERFORMANCE.md` | Profiling-driven latency, CPU, and memory optimization. |
| `postmortem` | [`software-engineering/ops-performance/postmortem.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/postmortem.md) | `POSTMORTEM.md` | Blameless production incident root-cause analysis. |
| `review` | [`software-engineering/quality-security/review.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/review.md) | PR Feedback | Senior staff pull request review pass. |
| `schema` | [`software-engineering/architecture/schema.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/architecture/schema.md) | `SCHEMA_MIGRATION.md` | Zero-downtime database DDL schema evolution. |
| `security` | [`software-engineering/quality-security/security.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/security.md) | `SECURITY.md` | AppSec audit targeting injection, AuthN/AuthZ & CORS. |
| `testing` | [`software-engineering/ops-performance/testing.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/testing.md) | Test Suite | Comprehensive unit, integration, and e2e test pass. |

---

### ⚔️ Dark Fantasy Worldbuilding (10 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `artifact` | [`worldbuilding/lore-systems/artifact.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/artifact.md) | Relic Lore | Cursed relics, weapons, or ancient mechanisms. |
| `bestiary` | [`worldbuilding/entities/bestiary.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/entities/bestiary.md) | Bestiary Entry | Clinical, biologically grounded creature entry. |
| `bloodline` | [`worldbuilding/factions-beliefs/bloodline.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/bloodline.md) | Dynasty Lore | Cursed lineages, dynasties, and family secrets. |
| `character` | [`worldbuilding/entities/character.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/entities/character.md) | Character Profile | Key NPC, historical legend, tyrant, or hero. |
| `event` | [`worldbuilding/lore-systems/event.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/event.md) | War Chronicle | Pivotal siege, battle, plague, or cosmic catastrophe. |
| `faction` | [`worldbuilding/factions-beliefs/faction.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/faction.md) | Institution Lore | Guilds, military orders, cabals, and empires. |
| `location` | [`worldbuilding/lore-systems/location.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/location.md) | Cartography Entry | Fortresses, ruined cities, dungeons, and regions. |
| `magic` | [`worldbuilding/lore-systems/magic.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/magic.md) | Arcane Lorebook | Magic systems defined by finite Source and Toll. |
| `pantheon` | [`worldbuilding/factions-beliefs/pantheon.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/pantheon.md) | Cosmic Lorebook | Deities, cosmic horrors, and planar hierarchy. |
| `religion` | [`worldbuilding/factions-beliefs/religion.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/religion.md) | Theology Record | Cults, churches, dogmas, and religious heresies. |

---

## 🛠️ CLI Utilities & Tooling

### 1. Validate Prompt Suite
Verify all 42 prompts exist and conform to XML tag specifications:
```bash
python3 validate_prompts.py
```

### 2. Search & Filter Prompts
Query the repository by keyword, domain, or subcategory:
```bash
# Search by keyword
python3 search_prompts.py security

# Filter by domain
python3 search_prompts.py --domain android

# Filter by domain and keyword
python3 search_prompts.py migration --domain software-engineering
```

---

## 🔄 Legacy Filename Reference

For users familiar with the original unorganized filenames, refer to this mapping:

| Original Flat Filename | New Modular Path |
|---|---|
| `A11Y-PROMPT.md` | [`software-engineering/quality-security/a11y.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/a11y.md) |
| `ANDROID-A11Y-PROMPT.md` | [`android/quality-security/android-a11y.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-a11y.md) |
| `ANDROID-ARCHITECTURE-PROMPT.md` | [`android/architecture-refactoring/android-architecture.md`](file:///home/sysadmin/Downloads/shed-prompts/android/architecture-refactoring/android-architecture.md) |
| `ANDROID-AUDIT-PROMPT.md` | [`android/quality-security/android-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-audit.md) |
| `ANDROID-DEPENDENCY-PROMPT.md` | [`android/ops-performance/android-dependency.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-dependency.md) |
| `ANDROID-I18N-PROMPT.md` | [`android/ops-performance/android-i18n.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-i18n.md) |
| `ANDROID-MIGRATION-PROMPT.md` | [`android/architecture-refactoring/android-migration.md`](file:///home/sysadmin/Downloads/shed-prompts/android/architecture-refactoring/android-migration.md) |
| `ANDROID-OBSERVABILITY-PROMPT.md` | [`android/ops-performance/android-observability.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-observability.md) |
| `ANDROID-PERFORMANCE-PROMPT.md` | [`android/ops-performance/android-performance.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-performance.md) |
| `ANDROID-PERMISSIONS-PROMPT.md` | [`android/quality-security/android-permissions.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-permissions.md) |
| `ANDROID-RELEASE-PROMPT.md` | [`android/ops-performance/android-release.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-release.md) |
| `ANDROID-SECURITY-PROMPT.md` | [`android/quality-security/android-security.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-security.md) |
| `ANDROID-TESTING-PROMPT.md` | [`android/quality-security/android-testing.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-testing.md) |
| `ARTIFACT-PROMPT.md` | [`worldbuilding/lore-systems/artifact.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/artifact.md) |
| `AUDIT-IMPLEMENTATION-PROMPT.md` | [`software-engineering/quality-security/audit-implementation.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/audit-implementation.md) |
| `AUDIT-PROMPT.md` | [`software-engineering/quality-security/audit.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/audit.md) |
| `BESTIARY-PROMPT.md` | [`worldbuilding/entities/bestiary.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/entities/bestiary.md) |
| `BLOODLINE-PROMPT.md` | [`worldbuilding/factions-beliefs/bloodline.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/bloodline.md) |
| `BUNDLE-PROMPT.md` | [`software-engineering/ops-performance/bundle.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/bundle.md) |
| `CHANGELOG-PROMPT.md` | [`software-engineering/ops-performance/changelog.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/changelog.md) |
| `CHARACTER-PROMPT.md` | [`worldbuilding/entities/character.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/entities/character.md) |
| `DEPENDENCY-PROMPT.md` | [`software-engineering/quality-security/dependency.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/dependency.md) |
| `EVENT-PROMPT.md` | [`worldbuilding/lore-systems/event.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/event.md) |
| `FACTION-PROMPT.md` | [`worldbuilding/factions-beliefs/faction.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/faction.md) |
| `FEATURE-PROMPT.md` | [`software-engineering/product-strategy/feature.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/product-strategy/feature.md) |
| `I18N-PROMPT.md` | [`software-engineering/ops-performance/i18n.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/i18n.md) |
| `IDEATION-PROMPT.md` | [`software-engineering/product-strategy/ideation.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/product-strategy/ideation.md) |
| `IMPROVEMENT-PROMPT.md` | [`software-engineering/product-strategy/improvement.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/product-strategy/improvement.md) |
| `LOCATION-PROMPT.md` | [`worldbuilding/lore-systems/location.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/location.md) |
| `MAGIC-PROMPT.md` | [`worldbuilding/lore-systems/magic.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/magic.md) |
| `MIGRATION-PROMPT.md` | [`software-engineering/architecture/migration.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/architecture/migration.md) |
| `MODULARIZE-PROMPT.md` | [`software-engineering/architecture/modularize.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/architecture/modularize.md) |
| `OBSERVABILITY-PROMPT.md` | `software-engineering/ops-performance/observability.md` |
| `ONBOARDING-PROMPT.md` | [`software-engineering/product-strategy/onboarding.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/product-strategy/onboarding.md) |
| `PANTHEON-PROMPT.md` | [`worldbuilding/factions-beliefs/pantheon.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/pantheon.md) |
| `PERFORMANCE-PROMPT.md` | [`software-engineering/ops-performance/performance.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/performance.md) |
| `POSTMORTEM-PROMPT.md` | [`software-engineering/ops-performance/postmortem.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/postmortem.md) |
| `RELIGION-PROMPT.md` | [`worldbuilding/factions-beliefs/religion.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/religion.md) |
| `REVIEW-PROMPT.md` | [`software-engineering/quality-security/review.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/review.md) |
| `SCHEMA-PROMPT.md` | [`software-engineering/architecture/schema.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/architecture/schema.md) |
| `SECURITY-PROMPT.md` | [`software-engineering/quality-security/security.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/security.md) |
| `TESTING-PROMPT.md` | [`software-engineering/ops-performance/testing.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/testing.md) |
