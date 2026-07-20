# 📚 Shed Prompts: Modular Prompt Architecture Library

Welcome to **Shed Prompts**. This collection provides 193 battle-tested, high-precision system prompts categorized into modular domain hierarchies: **Android Engineering**, **General Software Engineering**, **Data & Analytics**, **Dark Fantasy RPG Worldbuilding**, **Autobiography & Memoir Co-Creation**, **Accelerated Learning & Pedagogical Architecture**, **Product Leadership & Venture Architecture**, **Legal Tech, Regulatory Compliance & IP Audit**, **Local Safetensor Model Fine-Tuning**, **Custom AI Architecture & LLM Engineering**, **Open-Weight Music & Audio Generation**, **Open-Weight Local Image Generation**, **Open-Weight Local Video Generation**, **Game Development & Interactive Systems**, and **DevOps, Cloud Infrastructure & SRE, and Scientific Method, Research & Academic Publishing**.

Each prompt is designed to act as an autonomous agentic persona with strict `<system_instructions>`, workflow constraints, and deterministic `<output_format>` requirements.

---

<a id="top"></a>
## 📋 Table of Contents
- [🗂️ Directory Taxonomy](#-directory-taxonomy)
- [📑 Master Catalog](#-master-catalog)
  - [📱 Android Mobile Engineering (13 Prompts)](#android-mobile-engineering-13-prompts)
  - [💻 Software & System Engineering (27 Prompts)](#software-system-engineering-27-prompts)
  - [📊 Data & Analytics (10 Prompts)](#data-analytics-10-prompts)
  - [⚔️ Dark Fantasy Worldbuilding (11 Prompts)](#dark-fantasy-worldbuilding-11-prompts)
  - [📖 Autobiography & Memoir Co-Creation (17 Prompts)](#autobiography-memoir-co-creation-17-prompts)
  - [🔬 Scientific Method, Research & Academic Publishing (10 Prompts)](#scientific-method-research-academic-publishing-10-prompts)
  - [🎓 Accelerated Learning & Pedagogical Architecture (5 Prompts)](#accelerated-learning-pedagogical-architecture-5-prompts)
  - [⚖️ Legal Tech, Regulatory Compliance & IP Audit (13 Prompts)](#legal-tech-regulatory-compliance-ip-audit-13-prompts)
  - [⚙️ Safetensor Local Model Fine-Tuning (10 Prompts)](#safetensor-local-model-fine-tuning-10-prompts)
  - [🧠 Custom AI Architecture & LLM Engineering (10 Prompts)](#custom-ai-architecture-llm-engineering-10-prompts)
  - [🎵 Open-Weight Music & Audio Generation (8 Prompts)](#open-weight-music-audio-generation-8-prompts)
  - [🎨 Open-Weight Local Image Generation (7 Prompts)](#open-weight-local-image-generation-7-prompts)
  - [🎬 Open-Weight Local Video Generation (7 Prompts)](#open-weight-local-video-generation-7-prompts)
  - [💡 Product Leadership & Venture Architecture (13 Prompts)](#product-leadership-venture-architecture-13-prompts)
  - [🚀 DevOps, Cloud Infrastructure & SRE (16 Prompts)](#devops-cloud-infrastructure-sre-16-prompts)
  - [🕹️ Game Development & Interactive Systems (16 Prompts)](#game-development-interactive-systems-16-prompts)
- [🛠️ CLI Utilities & Tooling](#-cli-utilities--tooling)
- [🔄 Legacy Filename Reference](#-legacy-filename-reference)

---


## 🗂️ Directory Taxonomy

```
shed-prompts/
├── 🔬 academic-research/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── experimental-design/
│   │   ├── experimental-design-power.md
│   │   └── experimental-design-replication-auditor.md
│   ├── lit-synthesis/
│   │   ├── lit-synthesis-citation-network.md
│   │   ├── lit-synthesis-gap-tracker.md
│   │   ├── lit-synthesis-matrix.md
│   │   └── research-gap-finder.md
│   ├── manuscript-prep/
│   │   ├── manuscript-figure-caption-auditor.md
│   │   └── manuscript-latex-prep.md
│   └── peer-review-audit/
│       ├── peer-review-audit.md
│       └── peer-review-statistics-auditor.md
├── 📱 android/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── architecture-refactoring/
│   │   ├── android-architecture.md
│   │   ├── android-compose-migration-audit.md
│   │   └── android-migration.md
│   ├── ops-performance/
│   │   ├── android-dependency.md
│   │   ├── android-i18n.md
│   │   ├── android-observability.md
│   │   ├── android-performance.md
│   │   └── android-release.md
│   └── quality-security/
│       ├── android-a11y.md
│       ├── android-audit.md
│       ├── android-permissions.md
│       ├── android-security.md
│       └── android-testing.md
├── 📖 autobiography/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── crafting-polishing/
│   │   ├── autobiography-chapter-writer.md
│   │   ├── autobiography-chronology-audit.md
│   │   ├── autobiography-manuscript-assembly.md
│   │   ├── autobiography-prose-polish.md
│   │   └── autobiography-theme-extractor.md
│   ├── foundation-discovery/
│   │   ├── autobiography-interview.md
│   │   ├── autobiography-narrative-arc.md
│   │   └── autobiography-voice-tone.md
│   ├── life-stages/
│   │   ├── autobiography-ancestry-roots.md
│   │   ├── autobiography-career-vocation.md
│   │   ├── autobiography-formative-years.md
│   │   ├── autobiography-relationships-family.md
│   │   └── autobiography-turning-points.md
│   └── thematics-refinement/
│       ├── autobiography-adversity-resilience.md
│       ├── autobiography-legacy-reflections.md
│       ├── autobiography-memory-retrieval.md
│       └── autobiography-values-philosophy.md
├── 🧠 custom-ai/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── fine-tuning-quantization/
│   │   ├── custom-dataset-dedup-auditor.md
│   │   ├── custom-llm-fine-tuning-dataset-curator.md
│   │   ├── custom-lora-quantization.md
│   │   └── custom-quantization-loss-analyzer.md
│   ├── model-architecture/
│   │   ├── custom-attention-benchmark.md
│   │   ├── custom-attention-kv-cache.md
│   │   └── custom-transformer-swiglu.md
│   └── rag-evaluation/
│       ├── custom-rag-eval-pipeline.md
│       ├── custom-rag-hallucination-auditor.md
│       └── custom-rag-retrieval-coverage.md
├── 📊 data-analytics/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── analytics-engineering/
│   │   ├── analytics.md
│   │   ├── data-quality.md
│   │   ├── etl.md
│   │   ├── metrics.md
│   │   └── sql-query-optimizer.md
│   ├── experimentation/
│   │   ├── ab-test.md
│   │   └── reporting.md
│   ├── finops/
│   │   └── cost.md
│   └── visualization/
│       ├── charting.md
│       └── dashboard.md
├── 🚀 devops-sre/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── container-k8s/
│   │   ├── helm-chart-architecture.md
│   │   ├── ingress-service-mesh-config.md
│   │   ├── k8s-autoscaling-resource-tuning.md
│   │   └── k8s-security-posture-audit.md
│   ├── infrastructure-as-code/
│   │   ├── iac-drift-remediation-audit.md
│   │   ├── multi-region-cloud-topology.md
│   │   ├── terraform-opentofu-module.md
│   │   └── zero-trust-iam-audit.md
│   ├── pipeline-automation/
│   │   ├── artifact-signing-provenance.md
│   │   ├── canary-deployment-strategy.md
│   │   ├── hardened-ci-cd-pipeline.md
│   │   └── pipeline-vulnerability-containment.md
│   └── resilience-recovery/
│       ├── chaos-engineering-plan.md
│       ├── multi-az-failover-runbook.md
│       ├── rto-rpo-disaster-recovery-audit.md
│       └── slo-error-budget-automation.md
├── 🕹️ game-development/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── economy-balancing/
│   │   ├── damage-formula-optimizer.md
│   │   ├── economy-sink-source-audit.md
│   │   ├── loot-table-balancer.md
│   │   └── progression-curve-modeler.md
│   ├── engine-systems/
│   │   ├── ecs-architecture-audit.md
│   │   ├── engine-systems-conformance-audit.md
│   │   ├── physics-collision-spec.md
│   │   └── state-machine-blueprint.md
│   ├── graphics-performance/
│   │   ├── draw-call-optimizer.md
│   │   ├── memory-budget-enforcer.md
│   │   ├── mobile-console-target-profiler.md
│   │   └── shader-profiling-audit.md
│   └── level-design/
│       ├── environmental-puzzle-mechanics.md
│       ├── greybox-spatial-blueprint.md
│       ├── pacing-map-generator.md
│       └── player-flow-diagram.md
├── 🎨 image-generation/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── conditioned-generation/
│   │   ├── controlnet-ipadapter-pipeline.md
│   │   ├── image-controlnet-depth-auditor.md
│   │   └── image-inpainting-mask-auditor.md
│   └── diffusers-pipelines/
│       ├── flux-diffusers-pipeline.md
│       ├── image-lora-stack-composer.md
│       ├── prompt-expansion-matrix.md
│       └── sdxl-pipeline.md
├── ⚖️ legal-compliance/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── contract-risk/
│   │   ├── contract-negotiation-playbook.md
│   │   ├── contract-risk-deconstruction.md
│   │   └── contract-termination-exit.md
│   ├── ip-licensing/
│   │   ├── dual-license-patent.md
│   │   ├── ip-provenance-inventory.md
│   │   └── oss-license-conflict-audit.md
│   ├── policy-frameworks/
│   │   ├── data-classification.md
│   │   ├── sla-architecture.md
│   │   └── soc2-iso27001-policy.md
│   └── privacy-compliance/
│       ├── ai-act-conformance.md
│       ├── data-retention-consent.md
│       ├── gdpr-dpia-assessment.md
│       └── privacy-regulatory-audit.md
├── 🎵 music-generation/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── audio-diffusion-stem/
│   │   ├── audioldm-stem-pipeline.md
│   │   ├── music-stem-loudness-normalizer.md
│   │   └── music-stem-separation-auditor.md
│   └── text-to-music/
│       ├── music-arranger-prompt-suite.md
│       ├── music-genre-prompt-auditor.md
│       ├── music-structure-sectioner.md
│       ├── musicgen-pipeline.md
│       └── stable-audio-pipeline.md
├── 🎓 pedagogy-learning/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── curriculum-design/
│   │   └── curriculum-blueprint.md
│   ├── flashcard-systems/
│   │   ├── anki-fact-extractor.md
│   │   └── spaced-repetition-deck-generator.md
│   ├── skill-diagnostics/
│   │   └── diagnostic-gap-audit.md
│   └── socratic-drills/
│       └── socratic-interrogation.md
├── 💡 product-venture/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── discovery-intelligence/
│   │   ├── incumbent-teardown.md
│   │   ├── interview-synthesis.md
│   │   ├── market-opportunity-map.md
│   │   └── pain-point-extraction.md
│   ├── gtm-launch/
│   │   ├── beta-feedback-loop.md
│   │   ├── onboarding-funnel.md
│   │   └── producthunt-launch-kit.md
│   ├── monetization-pricing/
│   │   ├── cac-ltv-payback.md
│   │   ├── monetization-risk-audit.md
│   │   └── saas-pricing-modeler.md
│   └── product-specs/
│       ├── edge-case-matrix.md
│       ├── prd-generator.md
│       └── user-story-matrix.md
├── ⚙️ safetensor-fine-tuning/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── linux/
│   │   ├── linux-safetensor-env.md
│   │   ├── linux-safetensor-pipeline.md
│   │   ├── linux-safetensor-quantization.md
│   │   └── safetensor-metadata-audit.md
│   ├── mac/
│   │   ├── mac-safetensor-env.md
│   │   ├── mac-safetensor-pipeline.md
│   │   └── mac-safetensor-quantization.md
│   └── windows/
│       ├── windows-safetensor-env.md
│       ├── windows-safetensor-pipeline.md
│       └── windows-safetensor-quantization.md
├── 💻 software-engineering/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── architecture/
│   │   ├── git-repo-health-audit.md
│   │   ├── migration.md
│   │   ├── modularize.md
│   │   └── schema.md
│   ├── ops-performance/
│   │   ├── api-docs.md
│   │   ├── bundle.md
│   │   ├── changelog.md
│   │   ├── i18n.md
│   │   ├── license.md
│   │   ├── observability.md
│   │   ├── performance.md
│   │   ├── postmortem.md
│   │   ├── runbook.md
│   │   ├── seo.md
│   │   ├── slo.md
│   │   ├── testing.md
│   │   └── threat-model.md
│   ├── product-strategy/
│   │   ├── feature.md
│   │   ├── ideation.md
│   │   ├── improvement.md
│   │   └── onboarding.md
│   └── quality-security/
│       ├── a11y.md
│       ├── audit-implementation.md
│       ├── audit.md
│       ├── dependency.md
│       ├── review.md
│       └── security.md
├── 🎬 video-generation/
│   ├── README.md                   # Category overview & pipeline guide
│   ├── image-to-video/
│   │   ├── svd-image-to-video-pipeline.md
│   │   └── video-frame-consistency-auditor.md
│   └── text-to-video/
│       ├── animatediff-pipeline.md
│       ├── cogvideox-pipeline.md
│       ├── video-motion-coherence-auditor.md
│       ├── video-prompt-storyboard-auditor.md
│       └── video-storyboard-pipeline.md
└── ⚔️ worldbuilding/
    ├── README.md                   # Category overview & pipeline guide
    ├── entities/
    │   ├── bestiary.md
    │   └── character.md
    ├── factions-beliefs/
    │   ├── bloodline.md
    │   ├── faction.md
    │   ├── pantheon.md
    │   └── religion.md
    └── lore-systems/
        ├── artifact.md
        ├── event.md
        ├── location.md
        ├── magic.md
        └── world-timeline-chronicle.md
```


---

[⬆ Back to Top](#top)

---
## 📑 Master Catalog

---
### 📱 Android Mobile Engineering (13 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `android-a11y` | [`android/quality-security/android-a11y.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-a11y.md) | `ANDROID_A11Y.md` | You are an Accessibility Engineer performing an Android accessibility compliance audit and remediation pass, targeting WCAG 2 |
| `android-architecture` | [`android/architecture-refactoring/android-architecture.md`](file:///home/sysadmin/Downloads/shed-prompts/android/architecture-refactoring/android-architecture.md) | `ANDROID_ARCHITECTURE.md` | You are a Principal Android Engineer designing or evaluating the architecture of an Android application (Kotlin, Jetpack, Gradle) |
| `android-audit` | [`android/quality-security/android-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-audit.md) | `ANDROID_AUDIT.md` | You are a Lead Android Engineer performing a strict, read-only code quality audit of an Android codebase (Kotlin/Java, Gradle) |
| `android-compose-migration-audit` | [`android/architecture-refactoring/android-compose-migration-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/android/architecture-refactoring/android-compose-migration-audit.md) | `ANDROID_COMPOSE_MIGRATION_AUDIT.md` | Autonomous static audit & jetpack compose refactoring blueprint for legacy Android XML layouts and views |
| `android-dependency` | [`android/ops-performance/android-dependency.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-dependency.md) | `ANDROID_DEPENDENCY_REPORT.md` | You are an expert Dependency and Security Engineer for an Android/Gradle project |
| `android-i18n` | [`android/ops-performance/android-i18n.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-i18n.md) | `ANDROID_I18N.md` | You are an Internationalization Engineer preparing an Android app for multi-locale and RTL support |
| `android-migration` | [`android/architecture-refactoring/android-migration.md`](file:///home/sysadmin/Downloads/shed-prompts/android/architecture-refactoring/android-migration.md) | `ANDROID_MIGRATION.md` | You are a Lead Android Engineer executing a deliberate, breaking-change migration — a `targetSdkVersion` bump, Java→Kotlin conversion, View system→Jetpack Compose migration, or a major library's API contract change (e |
| `android-observability` | [`android/ops-performance/android-observability.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-observability.md) | `ANDROID_OBSERVABILITY.md` | You are a Site Reliability Engineer performing an observability instrumentation pass on an Android app |
| `android-performance` | [`android/ops-performance/android-performance.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-performance.md) | `ANDROID_PERFORMANCE.md` | You are a Performance Engineer performing a profiling-driven optimization pass on an Android application |
| `android-permissions` | [`android/quality-security/android-permissions.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-permissions.md) | `ANDROID_PERMISSIONS.md` | You are an Android Platform Engineer performing a permissions and runtime-privacy audit |
| `android-release` | [`android/ops-performance/android-release.md`](file:///home/sysadmin/Downloads/shed-prompts/android/ops-performance/android-release.md) | `ANDROID_RELEASE.md` | You are a Lead Release Engineer taking an Android project from its current state to a signed, Play-Store-ready App Bundle (AAB) and/or installable APK in a single autonomous pass |
| `android-security` | [`android/quality-security/android-security.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-security.md) | `ANDROID_SECURITY.md` | You are a Principal Application Security Engineer performing a strict Android/APK security audit and remediation pass |
| `android-testing` | [`android/quality-security/android-testing.md`](file:///home/sysadmin/Downloads/shed-prompts/android/quality-security/android-testing.md) | `ANDROID_TESTING.md` | You are a Principal Android Engineer and Testing Architect executing a comprehensive, project-wide testing run across unit, instrumented, and UI test layers |

---

[⬆ Back to Top](#top)

---
### 💻 Software & System Engineering (27 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `a11y` | [`software-engineering/quality-security/a11y.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/a11y.md) | `A11Y.md` | You are an Accessibility Engineer performing a WCAG 2 |
| `api-docs` | [`software-engineering/ops-performance/api-docs.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/api-docs.md) | `API_DOCS.md` | You are a Technical Writer generating OpenAPI and reference docs from real endpoints |
| `audit` | [`software-engineering/quality-security/audit.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/audit.md) | `AUDIT.md` | You are a Lead Software Engineer performing a strict, read-only code quality audit |
| `audit-implementation` | [`software-engineering/quality-security/audit-implementation.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/audit-implementation.md) | `N/A` | You are a Principal Software Engineer executing a rigorous code implementation run |
| `bundle` | [`software-engineering/ops-performance/bundle.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/bundle.md) | `RELEASE.md` | You are a Lead Release Engineer |
| `changelog` | [`software-engineering/ops-performance/changelog.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/changelog.md) | `N/A` | You are a Release Manager generating a `CHANGELOG |
| `dependency` | [`software-engineering/quality-security/dependency.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/dependency.md) | `N/A` | You are an expert Dependency and Security Engineer |
| `feature` | [`software-engineering/product-strategy/feature.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/product-strategy/feature.md) | `N/A` | You are a Lead Product Engineer |
| `git-repo-health-audit` | [`software-engineering/architecture/git-repo-health-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/architecture/git-repo-health-audit.md) | `GIT_REPO_HEALTH_AUDIT.md` | Autonomous git codebase health, architectural debt, and test coverage gap auditor with automated remediation roadmap |
| `i18n` | [`software-engineering/ops-performance/i18n.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/i18n.md) | `I18N.md` | You are an Internationalization (i18n) Engineer preparing this codebase for multi-locale support |
| `ideation` | [`software-engineering/product-strategy/ideation.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/product-strategy/ideation.md) | `N/A` | You are a Principal Product Strategist and Technical Feasibility Assessor operating with full autonomy |
| `improvement` | [`software-engineering/product-strategy/improvement.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/product-strategy/improvement.md) | `N/A` | You are a Principal Software Engineer executing a proactive code improvement and stabilization run |
| `license` | [`software-engineering/ops-performance/license.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/license.md) | `LICENSE_AUDIT.md` | You are an OSS License Compliance Engineer auditing copyleft risk and conflicts |
| `migration` | [`software-engineering/architecture/migration.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/architecture/migration.md) | `MIGRATION.md` | You are a Lead Software Engineer executing a deliberate, breaking-change migration — a major framework, runtime, or library version upgrade (e |
| `modularize` | [`software-engineering/architecture/modularize.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/architecture/modularize.md) | `MODULARIZATION.md` | You are a Lead Software Architect performing a structural refactor |
| `observability` | [`software-engineering/ops-performance/observability.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/observability.md) | `OBSERVABILITY.md` | You are a Site Reliability Engineer performing an observability instrumentation pass |
| `onboarding` | [`software-engineering/product-strategy/onboarding.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/product-strategy/onboarding.md) | `N/A` | You are a Principal Staff Engineer creating or updating the `ONBOARDING |
| `performance` | [`software-engineering/ops-performance/performance.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/performance.md) | `PERFORMANCE.md` | You are a Performance Engineer performing a profiling-driven optimization pass |
| `postmortem` | [`software-engineering/ops-performance/postmortem.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/postmortem.md) | `POSTMORTEM.md` | You are a Site Reliability Engineer writing a blameless postmortem for a production incident |
| `review` | [`software-engineering/quality-security/review.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/review.md) | `N/A` | You are a Staff Software Engineer performing a pull request review |
| `runbook` | [`software-engineering/ops-performance/runbook.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/runbook.md) | `RUNBOOK.md` | You are a Site Reliability Engineer generating an autonomous incident runbook |
| `schema` | [`software-engineering/architecture/schema.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/architecture/schema.md) | `SCHEMA_MIGRATION.md` | You are a Database Engineer executing a schema evolution with zero-downtime as a hard requirement |
| `security` | [`software-engineering/quality-security/security.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/quality-security/security.md) | `SECURITY.md` | You are a Principal Application Security Engineer performing a strict security audit and remediation pass |
| `seo` | [`software-engineering/ops-performance/seo.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/seo.md) | `SEO.md` | You are an SEO Engineer performing a technical SEO crawl, metadata, and Core Web Vitals audit |
| `slo` | [`software-engineering/ops-performance/slo.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/slo.md) | `SLO.md` | You are a Site Reliability Engineer defining SLOs, SLIs, and error-budget policy from telemetry |
| `testing` | [`software-engineering/ops-performance/testing.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/testing.md) | `N/A` | You are a Principal Software Engineer and Testing Architect executing a comprehensive, project-wide testing run |
| `threat-model` | [`software-engineering/ops-performance/threat-model.md`](file:///home/sysadmin/Downloads/shed-prompts/software-engineering/ops-performance/threat-model.md) | `THREAT_MODEL.md` | You are a Principal Application Security Engineer performing a STRIDE threat-modeling pass |

---

[⬆ Back to Top](#top)

---
### 📊 Data & Analytics (10 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `ab-test` | [`data-analytics/experimentation/ab-test.md`](file:///home/sysadmin/Downloads/shed-prompts/data-analytics/experimentation/ab-test.md) | `EXPERIMENT.md` | You are an Experimentation Scientist designing powered A/B tests and analyzing results |
| `analytics` | [`data-analytics/analytics-engineering/analytics.md`](file:///home/sysadmin/Downloads/shed-prompts/data-analytics/analytics-engineering/analytics.md) | `ANALYTICS.md` | You are an Analytics Engineer performing an event-tracking audit and building a consolidated tracking plan for this codebase |
| `charting` | [`data-analytics/visualization/charting.md`](file:///home/sysadmin/Downloads/shed-prompts/data-analytics/visualization/charting.md) | `CHARTS.md` | You are a Data Visualization Engineer generating honest, reproducible charts from datasets |
| `cost` | [`data-analytics/finops/cost.md`](file:///home/sysadmin/Downloads/shed-prompts/data-analytics/finops/cost.md) | `COST_ANALYSIS.md` | You are a FinOps / Cloud Cost Engineer analyzing spend and recommending optimizations |
| `dashboard` | [`data-analytics/visualization/dashboard.md`](file:///home/sysadmin/Downloads/shed-prompts/data-analytics/visualization/dashboard.md) | `DASHBOARD.md` | You are an Analytics / BI Engineer specifying a metrics dashboard wired to real data sources |
| `data-quality` | [`data-analytics/analytics-engineering/data-quality.md`](file:///home/sysadmin/Downloads/shed-prompts/data-analytics/analytics-engineering/data-quality.md) | `DATA_QUALITY.md` | You are a Data Quality Engineer performing a read-only data profiling and validation pass |
| `etl` | [`data-analytics/analytics-engineering/etl.md`](file:///home/sysadmin/Downloads/shed-prompts/data-analytics/analytics-engineering/etl.md) | `PIPELINE.md` | You are a Data Engineer building or refactoring an idempotent, observable pipeline |
| `metrics` | [`data-analytics/analytics-engineering/metrics.md`](file:///home/sysadmin/Downloads/shed-prompts/data-analytics/analytics-engineering/metrics.md) | `METRICS.md` | You are a Metrics & Analytics Lead defining and normalizing a canonical KPI/metric taxonomy |
| `reporting` | [`data-analytics/experimentation/reporting.md`](file:///home/sysadmin/Downloads/shed-prompts/data-analytics/experimentation/reporting.md) | `REPORT.md` | You are a Data Analyst producing an autonomous periodic insight and KPI movement report |
| `sql-query-optimizer` | [`data-analytics/analytics-engineering/sql-query-optimizer.md`](file:///home/sysadmin/Downloads/shed-prompts/data-analytics/analytics-engineering/sql-query-optimizer.md) | `SQL_QUERY_OPTIMIZATION_PLAN.md` | Autonomous SQL query performance profiler, CTE bottleneck analyzer, and zero-downtime index advisor |

---

[⬆ Back to Top](#top)

---
### ⚔️ Dark Fantasy Worldbuilding (11 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `artifact` | [`worldbuilding/lore-systems/artifact.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/artifact.md) | `N/A` | You are an expert worldbuilder and antiquarian for a Brutal Dark Medieval Fantasy RPG |
| `bestiary` | [`worldbuilding/entities/bestiary.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/entities/bestiary.md) | `N/A` | You are an expert worldbuilder and field naturalist for a Brutal Dark Medieval Fantasy RPG |
| `bloodline` | [`worldbuilding/factions-beliefs/bloodline.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/bloodline.md) | `N/A` | You are an expert worldbuilder and genealogical historian for a Brutal Dark Medieval Fantasy RPG |
| `character` | [`worldbuilding/entities/character.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/entities/character.md) | `N/A` | You are an expert worldbuilder and narrative designer for a Brutal Dark Medieval Fantasy RPG |
| `event` | [`worldbuilding/lore-systems/event.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/event.md) | `N/A` | You are an expert worldbuilder and war historian for a Brutal Dark Medieval Fantasy RPG |
| `faction` | [`worldbuilding/factions-beliefs/faction.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/faction.md) | `N/A` | You are an expert worldbuilder and institutional historian for a Brutal Dark Medieval Fantasy RPG |
| `location` | [`worldbuilding/lore-systems/location.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/location.md) | `N/A` | You are an expert worldbuilder and cartographic historian for a Brutal Dark Medieval Fantasy RPG |
| `magic` | [`worldbuilding/lore-systems/magic.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/magic.md) | `N/A` | You are an expert worldbuilder and arcane theorist for a Brutal Dark Medieval Fantasy RPG |
| `pantheon` | [`worldbuilding/factions-beliefs/pantheon.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/pantheon.md) | `N/A` | You are an expert worldbuilder and cosmologist for a Brutal Dark Medieval Fantasy RPG |
| `religion` | [`worldbuilding/factions-beliefs/religion.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/factions-beliefs/religion.md) | `N/A` | You are an expert worldbuilder and theological historian for a Brutal Dark Medieval Fantasy RPG |
| `world-timeline-chronicle` | [`worldbuilding/lore-systems/world-timeline-chronicle.md`](file:///home/sysadmin/Downloads/shed-prompts/worldbuilding/lore-systems/world-timeline-chronicle.md) | `WORLD_TIMELINE_CHRONICLE.md` | Autonomous fictional historical timeline chronicle, era designation synthesizer, and causality map generator |

---

[⬆ Back to Top](#top)

---
### 📖 Autobiography & Memoir Co-Creation (17 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `autobiography-adversity-resilience` | [`autobiography/thematics-refinement/autobiography-adversity-resilience.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/thematics-refinement/autobiography-adversity-resilience.md) | `AUTOBIOGRAPHY_ADVERSITY_RESILIENCE.md` | Deep exploration of hardship, grief, illness, vulnerability, and hard-won strength |
| `autobiography-ancestry-roots` | [`autobiography/life-stages/autobiography-ancestry-roots.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/life-stages/autobiography-ancestry-roots.md) | `AUTOBIOGRAPHY_ANCESTRY_ROOTS.md` | Ancestral heritage, family lineage, cultural roots, and childhood environment dossier |
| `autobiography-career-vocation` | [`autobiography/life-stages/autobiography-career-vocation.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/life-stages/autobiography-career-vocation.md) | `AUTOBIOGRAPHY_CAREER_VOCATION.md` | Professional journey, tradecraft mastery, leadership, career peaks, and setbacks |
| `autobiography-chapter-writer` | [`autobiography/crafting-polishing/autobiography-chapter-writer.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/crafting-polishing/autobiography-chapter-writer.md) | `AUTOBIOGRAPHY_CHAPTER.md` | Full chapter prose composition synthesizing interview notes into rich narrative arc |
| `autobiography-chronology-audit` | [`autobiography/crafting-polishing/autobiography-chronology-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/crafting-polishing/autobiography-chronology-audit.md) | `AUTOBIOGRAPHY_CHRONOLOGY_AUDIT.md` | Read-only timeline, age/date verification, fact-checking, and continuity audit |
| `autobiography-formative-years` | [`autobiography/life-stages/autobiography-formative-years.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/life-stages/autobiography-formative-years.md) | `AUTOBIOGRAPHY_FORMATIVE_YEARS.md` | Youth, adolescence, education, coming of age, and early identity formation |
| `autobiography-interview` | [`autobiography/foundation-discovery/autobiography-interview.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/foundation-discovery/autobiography-interview.md) | `AUTOBIOGRAPHY_INTERVIEW.md` | Empathetic oral history & life interview sessions with structured QA and memory extraction |
| `autobiography-legacy-reflections` | [`autobiography/thematics-refinement/autobiography-legacy-reflections.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/thematics-refinement/autobiography-legacy-reflections.md) | `AUTOBIOGRAPHY_LEGACY_REFLECTIONS.md` | Present-day reflections, letter to future generations, epilogue vision, and gratitude |
| `autobiography-manuscript-assembly` | [`autobiography/crafting-polishing/autobiography-manuscript-assembly.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/crafting-polishing/autobiography-manuscript-assembly.md) | `AUTOBIOGRAPHY_MANUSCRIPT_ASSEMBLY.md` | Full manuscript compilation, front/back matter, photo index, and production readiness |
| `autobiography-memory-retrieval` | [`autobiography/thematics-refinement/autobiography-memory-retrieval.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/thematics-refinement/autobiography-memory-retrieval.md) | `AUTOBIOGRAPHY_MEMORY_RETRIEVAL.md` | Sensory memory elicitation technique restoring sights, sounds, smells, and somatic feel |
| `autobiography-narrative-arc` | [`autobiography/foundation-discovery/autobiography-narrative-arc.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/foundation-discovery/autobiography-narrative-arc.md) | `AUTOBIOGRAPHY_NARRATIVE_ARC.md` | Master macro life narrative blueprint, themes, motifs, and act/chapter outline |
| `autobiography-prose-polish` | [`autobiography/crafting-polishing/autobiography-prose-polish.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/crafting-polishing/autobiography-prose-polish.md) | `AUTOBIOGRAPHY_PROSE_POLISH.md` | Line editing, sensory enhancement, pacing, rhythm, and stylistic refinement |
| `autobiography-relationships-family` | [`autobiography/life-stages/autobiography-relationships-family.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/life-stages/autobiography-relationships-family.md) | `AUTOBIOGRAPHY_RELATIONSHIPS_FAMILY.md` | Character portraits of partners, family, mentors, friends, and interpersonal dynamics |
| `autobiography-theme-extractor` | [`autobiography/crafting-polishing/autobiography-theme-extractor.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/crafting-polishing/autobiography-theme-extractor.md) | `AUTOBIOGRAPHY_THEME_INDEX.md` | Autonomous motif and emotional theme extractor across memoir chapters, transcripts, and personal notes |
| `autobiography-turning-points` | [`autobiography/life-stages/autobiography-turning-points.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/life-stages/autobiography-turning-points.md) | `AUTOBIOGRAPHY_TURNING_POINTS.md` | Watershed moments, crises, crossroads decisions, and transformational shifts |
| `autobiography-values-philosophy` | [`autobiography/thematics-refinement/autobiography-values-philosophy.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/thematics-refinement/autobiography-values-philosophy.md) | `AUTOBIOGRAPHY_VALUES_PHILOSOPHY.md` | Articulating personal philosophy, core values codex, and tested rules for living |
| `autobiography-voice-tone` | [`autobiography/foundation-discovery/autobiography-voice-tone.md`](file:///home/sysadmin/Downloads/shed-prompts/autobiography/foundation-discovery/autobiography-voice-tone.md) | `AUTOBIOGRAPHY_VOICE_TONE.md` | Defining author narrative voice, cadence, vocabulary, and linguistic style guide |

---

[⬆ Back to Top](#top)

---
### 🔬 Scientific Method, Research & Academic Publishing (10 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `experimental-design-power` | [`academic-research/experimental-design/experimental-design-power.md`](file:///home/sysadmin/Downloads/shed-prompts/academic-research/experimental-design/experimental-design-power.md) | `EXPERIMENTAL_DESIGN.md` | Defining control/treatment groups, confounding variables, sample-size justification, and statistical test recommendations before collecting data |
| `experimental-design-replication-auditor` | [`academic-research/experimental-design/experimental-design-replication-auditor.md`](file:///home/sysadmin/Downloads/shed-prompts/academic-research/experimental-design/experimental-design-replication-auditor.md) | `EXPERIMENTAL_DESIGN_REPLICATION_AUDIT.md` | Autonomous replication-crisis auditor scoring protocol reproducibility and missing controls. |
| `lit-synthesis-citation-network` | [`academic-research/lit-synthesis/lit-synthesis-citation-network.md`](file:///home/sysadmin/Downloads/shed-prompts/academic-research/lit-synthesis/lit-synthesis-citation-network.md) | `LIT_SYNTHESIS_CITATION_NETWORK.md` | Autonomous citation-network reconstruction and anomaly detection. |
| `lit-synthesis-gap-tracker` | [`academic-research/lit-synthesis/lit-synthesis-gap-tracker.md`](file:///home/sysadmin/Downloads/shed-prompts/academic-research/lit-synthesis/lit-synthesis-gap-tracker.md) | `LIT_SYNTHESIS_GAP_TRACKER.md` | Autonomous literature gap and contradiction clustering tracker. |
| `lit-synthesis-matrix` | [`academic-research/lit-synthesis/lit-synthesis-matrix.md`](file:///home/sysadmin/Downloads/shed-prompts/academic-research/lit-synthesis/lit-synthesis-matrix.md) | `LIT_SYNTHESIS_MATRIX.md` | Ingesting paper abstracts/summaries to produce a traceable matrix comparing methodologies, sample sizes, constraints, and conflicting results |
| `manuscript-figure-caption-auditor` | [`academic-research/manuscript-prep/manuscript-figure-caption-auditor.md`](file:///home/sysadmin/Downloads/shed-prompts/academic-research/manuscript-prep/manuscript-figure-caption-auditor.md) | `MANUSCRIPT_FIGURE_CAPTION_AUDITOR.md` | Autonomous figure caption and statistical-honesty auditor. |
| `manuscript-latex-prep` | [`academic-research/manuscript-prep/manuscript-latex-prep.md`](file:///home/sysadmin/Downloads/shed-prompts/academic-research/manuscript-prep/manuscript-latex-prep.md) | `MANUSCRIPT.md` | Formatting raw findings into journal-specific IMRaD structures with publication-ready figure captions and citations |
| `peer-review-audit` | [`academic-research/peer-review-audit/peer-review-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/academic-research/peer-review-audit/peer-review-audit.md) | `PEER_REVIEW_AUDIT.md` | Acting as an unsparing Reviewer #2 to attack methodology flaws, unbacked assertions, statistical overreach, and missing citations |
| `peer-review-statistics-auditor` | [`academic-research/peer-review-audit/peer-review-statistics-auditor.md`](file:///home/sysadmin/Downloads/shed-prompts/academic-research/peer-review-audit/peer-review-statistics-auditor.md) | `PEER_REVIEW_STATISTICS_AUDITOR.md` | Autonomous statistics-focused peer-review audit. |
| `research-gap-finder` | [`academic-research/lit-synthesis/research-gap-finder.md`](file:///home/sysadmin/Downloads/shed-prompts/academic-research/lit-synthesis/research-gap-finder.md) | `RESEARCH_GAP_ANALYSIS.md` | Autonomous domain research gap detector, novelty analysis, and high-impact hypothesis generator for academic literature |

---

[⬆ Back to Top](#top)

---
### 🎓 Accelerated Learning & Pedagogical Architecture (5 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `anki-fact-extractor` | [`pedagogy-learning/flashcard-systems/anki-fact-extractor.md`](file:///home/sysadmin/Downloads/shed-prompts/pedagogy-learning/flashcard-systems/anki-fact-extractor.md) | `ANKI_FLASHCARDS.md` | Extracting high-yield atomic facts from textbooks or papers and formatting them into optimal double-sided Anki cards with cloze deletions |
| `curriculum-blueprint` | [`pedagogy-learning/curriculum-design/curriculum-blueprint.md`](file:///home/sysadmin/Downloads/shed-prompts/pedagogy-learning/curriculum-design/curriculum-blueprint.md) | `CURRICULUM_BLUEPRINT.md` | Deconstructing dense topics into progressive 4-week mastery roadmaps using Bloom's Taxonomy and deliberate practice principles |
| `diagnostic-gap-audit` | [`pedagogy-learning/skill-diagnostics/diagnostic-gap-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/pedagogy-learning/skill-diagnostics/diagnostic-gap-audit.md) | `SKILL_DIAGNOSTIC_AUDIT.md` | Generating targeted diagnostic exams evaluating problem-solving intuition rather than rote memory with mistake-pattern analysis |
| `socratic-interrogation` | [`pedagogy-learning/socratic-drills/socratic-interrogation.md`](file:///home/sysadmin/Downloads/shed-prompts/pedagogy-learning/socratic-drills/socratic-interrogation.md) | `SOCRATIC_DRILL.md` | Interactive interrogation sessions testing first-principles understanding, Feynman Technique analogies, and knowledge gap discovery |
| `spaced-repetition-deck-generator` | [`pedagogy-learning/flashcard-systems/spaced-repetition-deck-generator.md`](file:///home/sysadmin/Downloads/shed-prompts/pedagogy-learning/flashcard-systems/spaced-repetition-deck-generator.md) | `SPACED_REPETITION_DECK.md` | Autonomous learning content condenser and atomic cloze-deletion flashcard deck generator for Anki and SRS |

---

[⬆ Back to Top](#top)

---
### ⚖️ Legal Tech, Regulatory Compliance & IP Audit (13 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `ai-act-conformance` | [`legal-compliance/privacy-compliance/ai-act-conformance.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/privacy-compliance/ai-act-conformance.md) | `AI_ACT_CONFORMANCE.md` | You are an AI Governance Engineer assessing an AI system against the EU AI Act risk tiers and obligations |
| `contract-negotiation-playbook` | [`legal-compliance/contract-risk/contract-negotiation-playbook.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/contract-risk/contract-negotiation-playbook.md) | `CONTRACT_NEGOTIATION_PLAYBOOK.md` | You are a Senior Commercial Contracts Negotiator converting audit findings into a prioritized redline-ready playbook |
| `contract-risk-deconstruction` | [`legal-compliance/contract-risk/contract-risk-deconstruction.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/contract-risk/contract-risk-deconstruction.md) | `CONTRACT_RISK_MATRIX.md` | You are a Commercial Contracts Counsel deconstructing agreements into indemnity, liability, and termination risk tables |
| `contract-termination-exit` | [`legal-compliance/contract-risk/contract-termination-exit.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/contract-risk/contract-termination-exit.md) | `CONTRACT_TERMINATION_AUDIT.md` | You are a Commercial Contracts Counsel auditing renewal, auto-renewal, exit penalties, and post-termination obligations |
| `data-classification` | [`legal-compliance/policy-frameworks/data-classification.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/policy-frameworks/data-classification.md) | `DATA_CLASSIFICATION_POLICY.md` | You are a Data Governance Architect authoring data-classification tiers, handling rules, and labeling enforcement |
| `data-retention-consent` | [`legal-compliance/privacy-compliance/data-retention-consent.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/privacy-compliance/data-retention-consent.md) | `DATA_RETENTION_CONSENT_REPORT.md` | You are a Privacy Engineer auditing data-retention schedules and consent-mechanism implementation |
| `dual-license-patent` | [`legal-compliance/ip-licensing/dual-license-patent.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/ip-licensing/dual-license-patent.md) | `DUAL_LICENSE_PATENT_REPORT.md` | You are an IP Licensing Counsel auditing dual-licensing elections and patent-retaliation clauses |
| `gdpr-dpia-assessment` | [`legal-compliance/privacy-compliance/gdpr-dpia-assessment.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/privacy-compliance/gdpr-dpia-assessment.md) | `GDPR_DPIA_ASSESSMENT.md` | Autonomous Data Protection Impact Assessment (DPIA) generator and privacy risk mitigation auditor |
| `ip-provenance-inventory` | [`legal-compliance/ip-licensing/ip-provenance-inventory.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/ip-licensing/ip-provenance-inventory.md) | `IP_PROVENANCE_INVENTORY.md` | You are an IP Asset Manager performing a read-only provenance inventory of first-party, third-party, and contributed code |
| `oss-license-conflict-audit` | [`legal-compliance/ip-licensing/oss-license-conflict-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/ip-licensing/oss-license-conflict-audit.md) | `OSS_LICENSE_CONFLICT_AUDIT.md` | You are an OSS License Compliance Engineer auditing GPL/AGPL/LGPL copyleft contamination against the distribution model |
| `privacy-regulatory-audit` | [`legal-compliance/privacy-compliance/privacy-regulatory-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/privacy-compliance/privacy-regulatory-audit.md) | `PRIVACY_COMPLIANCE_AUDIT.md` | You are a Privacy Engineer auditing architecture against GDPR, CCPA/CPRA, and the EU AI Act |
| `sla-architecture` | [`legal-compliance/policy-frameworks/sla-architecture.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/policy-frameworks/sla-architecture.md) | `SLA_ARCHITECTURE.md` | You are a Service-Level Architect drafting customer-facing SLA commitments, credits, and escalation paths |
| `soc2-iso27001-policy` | [`legal-compliance/policy-frameworks/soc2-iso27001-policy.md`](file:///home/sysadmin/Downloads/shed-prompts/legal-compliance/policy-frameworks/soc2-iso27001-policy.md) | `SECURITY_POLICY_FRAMEWORK.md` | You are a Security Architect drafting SOC 2 and ISO 27001 aligned internal security policies |

---

[⬆ Back to Top](#top)

---
### ⚙️ Safetensor Local Model Fine-Tuning (10 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `linux-safetensor-env` | [`safetensor-fine-tuning/linux/linux-safetensor-env.md`](file:///home/sysadmin/Downloads/shed-prompts/safetensor-fine-tuning/linux/linux-safetensor-env.md) | `LINUX_SAFETENSOR_ENV.md` | Principal AI Infrastructure Engineer configuring Linux CUDA/ROCm environments, driver stacks, PyTorch, xFormers, FlashAttention, and bitsandbytes for Safetensors fine-tuning |
| `linux-safetensor-pipeline` | [`safetensor-fine-tuning/linux/linux-safetensor-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/safetensor-fine-tuning/linux/linux-safetensor-pipeline.md) | `LINUX_SAFETENSOR_PIPELINE.md` | Senior ML Training Engineer orchestrating Linux LoRA/QLoRA and full parameter training pipelines, dataset tokenization, hyperparameters, and checkpointing for Safetensors models |
| `linux-safetensor-quantization` | [`safetensor-fine-tuning/linux/linux-safetensor-quantization.md`](file:///home/sysadmin/Downloads/shed-prompts/safetensor-fine-tuning/linux/linux-safetensor-quantization.md) | `LINUX_SAFETENSOR_QUANTIZATION.md` | Model Optimization Engineer handling adapter merging, safetensors integrity auditing, GGUF/EXL2/AWQ quantization, and local vLLM/Ollama inference validation on Linux |
| `mac-safetensor-env` | [`safetensor-fine-tuning/mac/mac-safetensor-env.md`](file:///home/sysadmin/Downloads/shed-prompts/safetensor-fine-tuning/mac/mac-safetensor-env.md) | `MAC_SAFETENSOR_ENV.md` | macOS Apple Silicon Systems Specialist configuring Metal Performance Shaders (MPS), MLX framework, sysctl unified memory limits, and Homebrew toolchains for Safetensors fine-tuning |
| `mac-safetensor-pipeline` | [`safetensor-fine-tuning/mac/mac-safetensor-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/safetensor-fine-tuning/mac/mac-safetensor-pipeline.md) | `MAC_SAFETENSOR_PIPELINE.md` | Apple Silicon ML Engineer executing MLX/LoRA and QLoRA fine-tuning workflows, dataset formatting, unified memory optimization, and MPS checkpointing for Safetensors models |
| `mac-safetensor-quantization` | [`safetensor-fine-tuning/mac/mac-safetensor-quantization.md`](file:///home/sysadmin/Downloads/shed-prompts/safetensor-fine-tuning/mac/mac-safetensor-quantization.md) | `MAC_SAFETENSOR_QUANTIZATION.md` | macOS Model Release Specialist merging MLX adapter weights into safetensors, performing metal float precision audits, GGUF quantization via native llama.cpp, and Ollama/LM Studio deployment |
| `safetensor-metadata-audit` | [`safetensor-fine-tuning/linux/safetensor-metadata-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/safetensor-fine-tuning/linux/safetensor-metadata-audit.md) | `SAFETENSOR_METADATA_AUDIT.md` | Autonomous safetensor model weights inspector, tensor shape sanity checker, and quantization readiness auditor |
| `windows-safetensor-env` | [`safetensor-fine-tuning/windows/windows-safetensor-env.md`](file:///home/sysadmin/Downloads/shed-prompts/safetensor-fine-tuning/windows/windows-safetensor-env.md) | `WINDOWS_SAFETENSOR_ENV.md` | Windows AI Systems Engineer setting up WSL2 CUDA drivers, native PyTorch, Windows pagefile management, bitsandbytes-windows binaries, and C++ build tools for Safetensors fine-tuning |
| `windows-safetensor-pipeline` | [`safetensor-fine-tuning/windows/windows-safetensor-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/safetensor-fine-tuning/windows/windows-safetensor-pipeline.md) | `WINDOWS_SAFETENSOR_PIPELINE.md` | Windows ML Engineer configuring Kohya_ss, LLaMA-Factory, and web UI/CLI workflows for LoRA/QLoRA fine-tuning of Safetensors models under Windows memory limits |
| `windows-safetensor-quantization` | [`safetensor-fine-tuning/windows/windows-safetensor-quantization.md`](file:///home/sysadmin/Downloads/shed-prompts/safetensor-fine-tuning/windows/windows-safetensor-quantization.md) | `WINDOWS_SAFETENSOR_QUANTIZATION.md` | Windows Model Deployment Engineer merging LoRA adapters into base Safetensors, verifying tensor precision, executing llama.cpp GGUF conversion, and loading into LM Studio/Ollama on Windows |

---

[⬆ Back to Top](#top)

---
### 🧠 Custom AI Architecture & LLM Engineering (10 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `custom-attention-benchmark` | [`custom-ai/model-architecture/custom-attention-benchmark.md`](file:///home/sysadmin/Downloads/shed-prompts/custom-ai/model-architecture/custom-attention-benchmark.md) | `CUSTOM_ATTENTION_BENCHMARK.md` | Autonomous attention-variant latency/memory/quality benchmark. |
| `custom-attention-kv-cache` | [`custom-ai/model-architecture/custom-attention-kv-cache.md`](file:///home/sysadmin/Downloads/shed-prompts/custom-ai/model-architecture/custom-attention-kv-cache.md) | `CUSTOM_ATTENTION_KV_CACHE_NOTEBOOK.ipynb` | You are a Principal AI Systems Engineer building Multi-Head/Grouped-Query Attention, RoPE, and KV Cache mechanisms in PyTorch |
| `custom-dataset-dedup-auditor` | [`custom-ai/fine-tuning-quantization/custom-dataset-dedup-auditor.md`](file:///home/sysadmin/Downloads/shed-prompts/custom-ai/fine-tuning-quantization/custom-dataset-dedup-auditor.md) | `CUSTOM_DATASET_DEDUP_AUDITOR.md` | Autonomous dataset deduplication and leakage auditor. |
| `custom-llm-fine-tuning-dataset-curator` | [`custom-ai/fine-tuning-quantization/custom-llm-fine-tuning-dataset-curator.md`](file:///home/sysadmin/Downloads/shed-prompts/custom-ai/fine-tuning-quantization/custom-llm-fine-tuning-dataset-curator.md) | `CUSTOM_DATASET_CURATION_REPORT.md` | Autonomous instruction tuning dataset curator, perplexity filter, and synthetic prompt quality auditor |
| `custom-lora-quantization` | [`custom-ai/fine-tuning-quantization/custom-lora-quantization.md`](file:///home/sysadmin/Downloads/shed-prompts/custom-ai/fine-tuning-quantization/custom-lora-quantization.md) | `CUSTOM_LORA_QUANTIZATION_NOTEBOOK.ipynb` | You are a Principal Applied AI & Quantization Specialist designing custom LoRA matrix injection and 4-bit quantization pipelines |
| `custom-quantization-loss-analyzer` | [`custom-ai/fine-tuning-quantization/custom-quantization-loss-analyzer.md`](file:///home/sysadmin/Downloads/shed-prompts/custom-ai/fine-tuning-quantization/custom-quantization-loss-analyzer.md) | `CUSTOM_QUANTIZATION_LOSS_ANALYZER.md` | Autonomous quantization loss and degradation analyzer. |
| `custom-rag-eval-pipeline` | [`custom-ai/rag-evaluation/custom-rag-eval-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/custom-ai/rag-evaluation/custom-rag-eval-pipeline.md) | `CUSTOM_RAG_EVAL_NOTEBOOK.ipynb` | You are a Lead AI Architect implementing dense/sparse hybrid RAG, Reciprocal Rank Fusion, and Ragas evaluation pipelines |
| `custom-rag-hallucination-auditor` | [`custom-ai/rag-evaluation/custom-rag-hallucination-auditor.md`](file:///home/sysadmin/Downloads/shed-prompts/custom-ai/rag-evaluation/custom-rag-hallucination-auditor.md) | `CUSTOM_RAG_HALLUCINATION_AUDITOR.md` | Autonomous RAG grounding and hallucination auditor. |
| `custom-rag-retrieval-coverage` | [`custom-ai/rag-evaluation/custom-rag-retrieval-coverage.md`](file:///home/sysadmin/Downloads/shed-prompts/custom-ai/rag-evaluation/custom-rag-retrieval-coverage.md) | `CUSTOM_RAG_RETRIEVAL_COVERAGE.md` | Autonomous RAG retrieval coverage and hole auditor. |
| `custom-transformer-swiglu` | [`custom-ai/model-architecture/custom-transformer-swiglu.md`](file:///home/sysadmin/Downloads/shed-prompts/custom-ai/model-architecture/custom-transformer-swiglu.md) | `CUSTOM_TRANSFORMER_SWIGLU_NOTEBOOK.ipynb` | You are an Expert LLM Neural Architecture Engineer implementing SwiGLU MLP layers, RMSNorm, and decoder blocks in PyTorch |

---

[⬆ Back to Top](#top)

---
### 🎵 Open-Weight Music & Audio Generation (8 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `audioldm-stem-pipeline` | [`music-generation/audio-diffusion-stem/audioldm-stem-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/music-generation/audio-diffusion-stem/audioldm-stem-pipeline.md) | `AUDIOLDM_STEM_NOTEBOOK.ipynb` | You are a Sound Design & Audio Engineer implementing AudioLDM 2 soundscape diffusion and Demucs stem separation pipelines |
| `music-arranger-prompt-suite` | [`music-generation/text-to-music/music-arranger-prompt-suite.md`](file:///home/sysadmin/Downloads/shed-prompts/music-generation/text-to-music/music-arranger-prompt-suite.md) | `MUSIC_ARRANGER_SUITE.md` | Autonomous multi-section music prompt arranger, stem structuring agent, and acoustic parameter generator for MusicGen and Suno |
| `music-genre-prompt-auditor` | [`music-generation/text-to-music/music-genre-prompt-auditor.md`](file:///home/sysadmin/Downloads/shed-prompts/music-generation/text-to-music/music-genre-prompt-auditor.md) | `MUSIC_GENRE_PROMPT_AUDITOR.md` | Autonomous genre/tempo/instrument prompt-fidelity auditor. |
| `music-stem-loudness-normalizer` | [`music-generation/audio-diffusion-stem/music-stem-loudness-normalizer.md`](file:///home/sysadmin/Downloads/shed-prompts/music-generation/audio-diffusion-stem/music-stem-loudness-normalizer.md) | `MUSIC_STEM_LOUDNESS_NORMALIZER.md` | Autonomous stem loudness (LUFS) normalizer. |
| `music-stem-separation-auditor` | [`music-generation/audio-diffusion-stem/music-stem-separation-auditor.md`](file:///home/sysadmin/Downloads/shed-prompts/music-generation/audio-diffusion-stem/music-stem-separation-auditor.md) | `MUSIC_STEM_SEPARATION_AUDITOR.md` | Autonomous stem-separation quality auditor. |
| `music-structure-sectioner` | [`music-generation/text-to-music/music-structure-sectioner.md`](file:///home/sysadmin/Downloads/shed-prompts/music-generation/text-to-music/music-structure-sectioner.md) | `MUSIC_STRUCTURE_SECTIONER.md` | Autonomous song-structure sectioner and arc checker. |
| `musicgen-pipeline` | [`music-generation/text-to-music/musicgen-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/music-generation/text-to-music/musicgen-pipeline.md) | `MUSICGEN_NOTEBOOK.ipynb` | You are an AI Audio & Music Generation Engineer building Meta MusicGen text-to-music and melody-guided steering pipelines |
| `stable-audio-pipeline` | [`music-generation/text-to-music/stable-audio-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/music-generation/text-to-music/stable-audio-pipeline.md) | `STABLE_AUDIO_NOTEBOOK.ipynb` | You are an Advanced Latent Audio Diffusion Specialist constructing Stable Audio Open text-to-audio diffusion pipelines |

---

[⬆ Back to Top](#top)

---
### 🎨 Open-Weight Local Image Generation (7 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `controlnet-ipadapter-pipeline` | [`image-generation/conditioned-generation/controlnet-ipadapter-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/image-generation/conditioned-generation/controlnet-ipadapter-pipeline.md) | `CONTROLNET_IPADAPTER_NOTEBOOK.ipynb` | You are a Conditioned Image Synthesis Specialist building ControlNet spatial control and IP-Adapter style steering diffusers pipelines |
| `flux-diffusers-pipeline` | [`image-generation/diffusers-pipelines/flux-diffusers-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/image-generation/diffusers-pipelines/flux-diffusers-pipeline.md) | `FLUX_DIFFUSERS_NOTEBOOK.ipynb` | You are a Next-Gen Image Synthesis Engineer constructing FLUX.1 [dev/schnell] flow matching pipelines with NF4/FP8 quantization |
| `image-controlnet-depth-auditor` | [`image-generation/conditioned-generation/image-controlnet-depth-auditor.md`](file:///home/sysadmin/Downloads/shed-prompts/image-generation/conditioned-generation/image-controlnet-depth-auditor.md) | `IMAGE_CONTROLNET_DEPTH_AUDITOR.md` | Autonomous ControlNet depth-fidelity auditor. |
| `image-inpainting-mask-auditor` | [`image-generation/conditioned-generation/image-inpainting-mask-auditor.md`](file:///home/sysadmin/Downloads/shed-prompts/image-generation/conditioned-generation/image-inpainting-mask-auditor.md) | `IMAGE_INPAINTING_MASK_AUDITOR.md` | Autonomous inpainting mask localization and seam auditor. |
| `image-lora-stack-composer` | [`image-generation/diffusers-pipelines/image-lora-stack-composer.md`](file:///home/sysadmin/Downloads/shed-prompts/image-generation/diffusers-pipelines/image-lora-stack-composer.md) | `IMAGE_LORA_STACK_COMPOSER.md` | Autonomous multi-LoRA stacking composer and bleed checker. |
| `prompt-expansion-matrix` | [`image-generation/diffusers-pipelines/prompt-expansion-matrix.md`](file:///home/sysadmin/Downloads/shed-prompts/image-generation/diffusers-pipelines/prompt-expansion-matrix.md) | `PROMPT_EXPANSION_MATRIX.md` | Autonomous prompt expander and aesthetic parameter generator for FLUX, SDXL, and Midjourney diffusion models |
| `sdxl-pipeline` | [`image-generation/diffusers-pipelines/sdxl-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/image-generation/diffusers-pipelines/sdxl-pipeline.md) | `SDXL_DIFFUSERS_NOTEBOOK.ipynb` | You are a Senior Computer Vision & Generative AI Engineer building SDXL Base + Refiner ensemble diffusers pipelines |

---

[⬆ Back to Top](#top)

---
### 🎬 Open-Weight Local Video Generation (7 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `animatediff-pipeline` | [`video-generation/text-to-video/animatediff-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/video-generation/text-to-video/animatediff-pipeline.md) | `ANIMATEDIFF_NOTEBOOK.ipynb` | You are an AnimateDiff & Motion Module Engineer constructing AnimateDiff motion adapter pipelines with prompt travel keyframing |
| `cogvideox-pipeline` | [`video-generation/text-to-video/cogvideox-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/video-generation/text-to-video/cogvideox-pipeline.md) | `COGVIDEOX_NOTEBOOK.ipynb` | You are an Open-Source Video Synthesis Specialist building CogVideoX (2B/5B) 3D transformer text-to-video diffusers pipelines |
| `svd-image-to-video-pipeline` | [`video-generation/image-to-video/svd-image-to-video-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/video-generation/image-to-video/svd-image-to-video-pipeline.md) | `SVD_IMAGE_TO_VIDEO_NOTEBOOK.ipynb` | You are a Temporal Latent Diffusion Specialist building Stable Video Diffusion (SVD-XT) image-to-video animation pipelines |
| `video-frame-consistency-auditor` | [`video-generation/image-to-video/video-frame-consistency-auditor.md`](file:///home/sysadmin/Downloads/shed-prompts/video-generation/image-to-video/video-frame-consistency-auditor.md) | `VIDEO_FRAME_CONSISTENCY_AUDITOR.md` | Autonomous image-to-video frame-consistency auditor. |
| `video-motion-coherence-auditor` | [`video-generation/text-to-video/video-motion-coherence-auditor.md`](file:///home/sysadmin/Downloads/shed-prompts/video-generation/text-to-video/video-motion-coherence-auditor.md) | `VIDEO_MOTION_COHERENCE_AUDITOR.md` | Autonomous video motion-coherence and jitter auditor. |
| `video-prompt-storyboard-auditor` | [`video-generation/text-to-video/video-prompt-storyboard-auditor.md`](file:///home/sysadmin/Downloads/shed-prompts/video-generation/text-to-video/video-prompt-storyboard-auditor.md) | `VIDEO_PROMPT_STORYBOARD_AUDITOR.md` | Autonomous video prompt storyboard and continuity auditor. |
| `video-storyboard-pipeline` | [`video-generation/text-to-video/video-storyboard-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/video-generation/text-to-video/video-storyboard-pipeline.md) | `VIDEO_STORYBOARD_PIPELINE.md` | Autonomous multi-shot video storyboard generator and cinematic prompt suite for Sora, CogVideoX, and Runway Gen-2 |

---

[⬆ Back to Top](#top)

---
### 💡 Product Leadership & Venture Architecture (13 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `beta-feedback-loop` | [`product-venture/gtm-launch/beta-feedback-loop.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/gtm-launch/beta-feedback-loop.md) | `BETA_FEEDBACK_LOOP.md` | Autonomous beta program design with feedback triage matrix, synthesis loop, and GA exit criteria |
| `cac-ltv-payback` | [`product-venture/monetization-pricing/cac-ltv-payback.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/monetization-pricing/cac-ltv-payback.md) | `CAC_LTV_PAYBACK.md` | Autonomous CAC/LTV computation, payback period, and churn sensitivity analysis for SaaS unit economics |
| `edge-case-matrix` | [`product-venture/product-specs/edge-case-matrix.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/product-specs/edge-case-matrix.md) | `EDGE_CASE_MATRIX.md` | Autonomous edge-case, abuse, and concurrency matrix with production telemetry and guardrail specification |
| `incumbent-teardown` | [`product-venture/discovery-intelligence/incumbent-teardown.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/discovery-intelligence/incumbent-teardown.md) | `INCUMBENT_TEARDOWN.md` | Autonomous reverse-engineering teardown of an incumbent product with competitive scorecard and wedge hypotheses |
| `interview-synthesis` | [`product-venture/discovery-intelligence/interview-synthesis.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/discovery-intelligence/interview-synthesis.md) | `INTERVIEW_SYNTHESIS.md` | Autonomous synthesis of user interviews into affinity themes, evidence-backed personas, and opportunity statements |
| `market-opportunity-map` | [`product-venture/discovery-intelligence/market-opportunity-map.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/discovery-intelligence/market-opportunity-map.md) | `MARKET_OPPORTUNITY_MAP.md` | Autonomous TAM/SAM/SOM sizing, segment matrix, and whitespace opportunity portfolio for a category |
| `monetization-risk-audit` | [`product-venture/monetization-pricing/monetization-risk-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/monetization-pricing/monetization-risk-audit.md) | `MONETIZATION_RISK_AUDIT.md` | Autonomous monetization strategy risk audit with exposure scoring and resilience grading A-F |
| `onboarding-funnel` | [`product-venture/gtm-launch/onboarding-funnel.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/gtm-launch/onboarding-funnel.md) | `ONBOARDING_FUNNEL.md` | Autonomous onboarding funnel design with aha-moment definition, instrumentation, and activation experiments |
| `pain-point-extraction` | [`product-venture/discovery-intelligence/pain-point-extraction.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/discovery-intelligence/pain-point-extraction.md) | `PAIN_POINT_EXTRACTION.md` | Autonomous pain-point extraction, severity x frequency scoring, and impact/effort prioritization matrix |
| `prd-generator` | [`product-venture/product-specs/prd-generator.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/product-specs/prd-generator.md) | `PRD.md` | Autonomous PRD generation with INVEST user stories, acceptance criteria, edge cases, and telemetry |
| `producthunt-launch-kit` | [`product-venture/gtm-launch/producthunt-launch-kit.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/gtm-launch/producthunt-launch-kit.md) | `PRODUCTHUNT_LAUNCH_KIT.md` | Autonomous Product Hunt and press-launch kit with assets, press release, and 14-day cadence |
| `saas-pricing-modeler` | [`product-venture/monetization-pricing/saas-pricing-modeler.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/monetization-pricing/saas-pricing-modeler.md) | `SAAS_PRICING_TIERS.md` | Autonomous SaaS pricing tier modeling, feature packaging matrix, and expansion-path design |
| `user-story-matrix` | [`product-venture/product-specs/user-story-matrix.md`](file:///home/sysadmin/Downloads/shed-prompts/product-venture/product-specs/user-story-matrix.md) | `USER_STORY_MATRIX.md` | Autonomous user-story and acceptance-criteria matrix with INVEST sizing and dependency mapping |

---

[⬆ Back to Top](#top)

---
### 🚀 DevOps, Cloud Infrastructure & SRE (16 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `artifact-signing-provenance` | [`devops-sre/pipeline-automation/artifact-signing-provenance.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/pipeline-automation/artifact-signing-provenance.md) | `ARTIFACT_SIGNING_PROVENANCE.md` | Automated container & binary artifact signing, Cosign verification, and SLSA provenance attestation architecture |
| `canary-deployment-strategy` | [`devops-sre/pipeline-automation/canary-deployment-strategy.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/pipeline-automation/canary-deployment-strategy.md) | `CANARY_DEPLOYMENT_STRATEGY.md` | Zero-downtime canary and progressive traffic shifting deployment strategy with automated rollback metrics |
| `chaos-engineering-plan` | [`devops-sre/resilience-recovery/chaos-engineering-plan.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/resilience-recovery/chaos-engineering-plan.md) | `CHAOS_ENGINEERING_PLAN.md` | Chaos engineering experiment design, blast radius control, fault injection hypothesis, and steady-state validation |
| `hardened-ci-cd-pipeline` | [`devops-sre/pipeline-automation/hardened-ci-cd-pipeline.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/pipeline-automation/hardened-ci-cd-pipeline.md) | `HARDENED_CI_CD_PIPELINE.md` | Hardened GitHub Actions / GitLab CI workflow architecture, OIDC secretless auth, and runner isolation spec |
| `helm-chart-architecture` | [`devops-sre/container-k8s/helm-chart-architecture.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/container-k8s/helm-chart-architecture.md) | `HELM_CHART_ARCHITECTURE.md` | Production Helm v3 chart architecture, value schema validation, and multi-environment override design |
| `iac-drift-remediation-audit` | [`devops-sre/infrastructure-as-code/iac-drift-remediation-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/infrastructure-as-code/iac-drift-remediation-audit.md) | `IAC_DRIFT_REMEDIATION_PLAN.md` | Autonomous Infrastructure as Code state drift detector, manual change scanner, and automated terraform import generator |
| `ingress-service-mesh-config` | [`devops-sre/container-k8s/ingress-service-mesh-config.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/container-k8s/ingress-service-mesh-config.md) | `INGRESS_SERVICE_MESH_SPEC.md` | Ingress controller and Istio/Linkerd service mesh configuration, mTLS enforcement, and traffic routing policy |
| `k8s-autoscaling-resource-tuning` | [`devops-sre/container-k8s/k8s-autoscaling-resource-tuning.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/container-k8s/k8s-autoscaling-resource-tuning.md) | `K8S_AUTOSCALING_TUNING_SPEC.md` | Kubernetes HPA/VPA autoscaling policies, pod resource request/limit profiling, and OOMKilled risk reduction |
| `k8s-security-posture-audit` | [`devops-sre/container-k8s/k8s-security-posture-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/container-k8s/k8s-security-posture-audit.md) | `K8S_SECURITY_POSTURE_AUDIT.md` | Autonomous Kubernetes cluster security posture auditor, RBAC privilege escalation scanner, and pod security standard verifier |
| `multi-az-failover-runbook` | [`devops-sre/resilience-recovery/multi-az-failover-runbook.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/resilience-recovery/multi-az-failover-runbook.md) | `MULTI_AZ_FAILOVER_RUNBOOK.md` | Multi-AZ and multi-region automated failover runbook, DNS failover routing, and database split-brain defense |
| `multi-region-cloud-topology` | [`devops-sre/infrastructure-as-code/multi-region-cloud-topology.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/infrastructure-as-code/multi-region-cloud-topology.md) | `MULTI_REGION_CLOUD_TOPOLOGY.md` | Multi-region cloud infrastructure topology specification, active-active networking, and VPC peering design |
| `pipeline-vulnerability-containment` | [`devops-sre/pipeline-automation/pipeline-vulnerability-containment.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/pipeline-automation/pipeline-vulnerability-containment.md) | `PIPELINE_VULNERABILITY_CONTAINMENT.md` | Autonomous CI/CD pipeline supply chain threat scanner, secret leak auditor, and dependency poisoning defense engine |
| `rto-rpo-disaster-recovery-audit` | [`devops-sre/resilience-recovery/rto-rpo-disaster-recovery-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/resilience-recovery/rto-rpo-disaster-recovery-audit.md) | `RTO_RPO_DISASTER_RECOVERY_AUDIT.md` | RTO/RPO disaster recovery audit, snapshot replication verifier, and cold/warm/hot restore protocol test |
| `slo-error-budget-automation` | [`devops-sre/resilience-recovery/slo-error-budget-automation.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/resilience-recovery/slo-error-budget-automation.md) | `SLO_ERROR_BUDGET_REPORT.md` | Autonomous SRE Service Level Objective (SLO) tracker, error budget burn rate analyzer, and deployment freeze advisory |
| `terraform-opentofu-module` | [`devops-sre/infrastructure-as-code/terraform-opentofu-module.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/infrastructure-as-code/terraform-opentofu-module.md) | `TERRAFORM_OPENTOFU_MODULE_SPEC.md` | Production Terraform/OpenTofu module architecture, variable validation, and state isolation design |
| `zero-trust-iam-audit` | [`devops-sre/infrastructure-as-code/zero-trust-iam-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/devops-sre/infrastructure-as-code/zero-trust-iam-audit.md) | `ZERO_TRUST_IAM_AUDIT.md` | Zero-Trust IAM security policy auditor, least-privilege role deconstruction, and privilege escalation detector |

---

[⬆ Back to Top](#top)

---
### 🕹️ Game Development & Interactive Systems (16 Prompts)
| Prompt ID | Relative Path | Target Artifact | Short Description |
|---|---|---|---|
| `damage-formula-optimizer` | [`game-development/economy-balancing/damage-formula-optimizer.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/economy-balancing/damage-formula-optimizer.md) | `DAMAGE_FORMULA_OPTIMIZER.md` | You are a Combat Systems Designer deriving a transparent, monotonically-bounded damage formula with mitigation, crit, variance, and TTK solver |
| `draw-call-optimizer` | [`game-development/graphics-performance/draw-call-optimizer.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/graphics-performance/draw-call-optimizer.md) | `DRAW_CALL_OPTIMIZER.md` | You are a Rendering Performance Engineer authoring a draw-call reduction plan via batching, instancing, and state-change ordering |
| `economy-sink-source-audit` | [`game-development/economy-balancing/economy-sink-source-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/economy-balancing/economy-sink-source-audit.md) | `ECONOMY_SINK_SOURCE_AUDIT.md` | You are an Autonomous Economy Auditor detecting inflation, dead sinks, and source/sink imbalance with no user input |
| `ecs-architecture-audit` | [`game-development/engine-systems/ecs-architecture-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/engine-systems/ecs-architecture-audit.md) | `ECS_ARCHITECTURE_AUDIT.md` | You are a Principal Game Engine Architect performing an autonomous ECS conformance audit for Unity DOTS, Unreal Mass, and Godot |
| `engine-systems-conformance-audit` | [`game-development/engine-systems/engine-systems-conformance-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/engine-systems/engine-systems-conformance-audit.md) | `ENGINE_SYSTEMS_CONFORMANCE_AUDIT.md` | You are an Autonomous Engine Systems Conformance Auditor for update ordering, lifecycle leaks, and streaming symmetry |
| `environmental-puzzle-mechanics` | [`game-development/level-design/environmental-puzzle-mechanics.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/level-design/environmental-puzzle-mechanics.md) | `ENVIRONMENTAL_PUZZLE_MECHANICS.md` | You are a Puzzle Designer authoring diegetic environmental mechanics with deterministic solve/fail states and soft-lock-free reset |
| `greybox-spatial-blueprint` | [`game-development/level-design/greybox-spatial-blueprint.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/level-design/greybox-spatial-blueprint.md) | `GREYBOX_SPATIAL_BLUEPRINT.md` | You are a Level Designer producing an annotated greybox spatial blueprint with cover arcs, sightlines, and traversal paths |
| `loot-table-balancer` | [`game-development/economy-balancing/loot-table-balancer.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/economy-balancing/loot-table-balancer.md) | `LOOT_TABLE_BALANCER.md` | You are a Game Economy Designer authoring weighted, seed-deterministic loot tables with pity floors and manipulation defense |
| `memory-budget-enforcer` | [`game-development/graphics-performance/memory-budget-enforcer.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/graphics-performance/memory-budget-enforcer.md) | `MEMORY_BUDGET_ENFORCER.md` | You are an Autonomous Memory Budget Enforcer auditing per-platform runtime caps, leaks, and headroom with no user input |
| `mobile-console-target-profiler` | [`game-development/graphics-performance/mobile-console-target-profiler.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/graphics-performance/mobile-console-target-profiler.md) | `MOBILE_CONSOLE_TARGET_PROFILER.md` | You are an Autonomous Target Profiler projecting frame budgets, thermal risk, and dynamic resolution across mobile and console SKUs |
| `pacing-map-generator` | [`game-development/level-design/pacing-map-generator.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/level-design/pacing-map-generator.md) | `PACING_MAP_GENERATOR.md` | You are a Narrative Pacing Designer generating a tension-curve pacing map sequencing combat, exploration, and rest beats |
| `physics-collision-spec` | [`game-development/engine-systems/physics-collision-spec.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/engine-systems/physics-collision-spec.md) | `PHYSICS_COLLISION_SPEC.md` | You are a Physics Engineer authoring a deterministic collision spec: collider topology, layer/mask matrix, and solver budget |
| `player-flow-diagram` | [`game-development/level-design/player-flow-diagram.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/level-design/player-flow-diagram.md) | `PLAYER_FLOW_DIAGRAM.md` | You are a Player Experience Architect modeling player flow and decision-path diagrams to expose friction and dead flow |
| `progression-curve-modeler` | [`game-development/economy-balancing/progression-curve-modeler.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/economy-balancing/progression-curve-modeler.md) | `PROGRESSION_CURVE_MODELER.md` | You are a Progression Designer modeling smooth XP/level curves with TTK-aligned power scaling and unlock cadence |
| `shader-profiling-audit` | [`game-development/graphics-performance/shader-profiling-audit.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/graphics-performance/shader-profiling-audit.md) | `SHADER_PROFILING_AUDIT.md` | You are an Autonomous Shader Profiler auditing HLSL/GLSL for ALU, bandwidth, divergence, and precision with no user input |
| `state-machine-blueprint` | [`game-development/engine-systems/state-machine-blueprint.md`](file:///home/sysadmin/Downloads/shed-prompts/game-development/engine-systems/state-machine-blueprint.md) | `STATE_MACHINE_BLUEPRINT.md` | You are a Gameplay Systems Designer authoring FSM/HSM blueprints with explicit transition tables and race resolution |

---

[⬆ Back to Top](#top)

---
## 🛠️ CLI Utilities & Tooling

### 1. Validate Prompt Suite
Verify all 193 prompts exist and conform to XML tag specifications:
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

---

[⬆ Back to Top](#top)
