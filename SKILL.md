---
name: plan-ios-app
description: Plan and de-risk native iOS app work with stronger design direction. Use when Codex needs to choose Swift as the default language for a new iOS app, decide between SwiftUI and UIKit, shape a distinctive UI art direction, choose system components or focused UI helpers, define theme colors and typography, or pick animation approaches like native SwiftUI motion, Lottie, Rive, or Hero. Trigger on requests about iOS app planning, 语言选择, 组件库, UI风格, 主题配色, 动画库, 视觉方案, 设计方向, 界面美化, or app 启动方案.
---

# Plan iOS App

## Overview

Use this skill before implementation when an iOS app idea is still vague or when UI direction stalls. Ask a short discovery set, default to the native Apple stack, and return a concrete build brief with stack, art direction, typography, layout language, color tokens, motion choice, and next steps.

## Workflow

1. Ask up to five short questions that will change the technical decision.
2. Commit to a clear visual point of view before naming libraries.
3. Decide the stack with a bias toward `Swift + SwiftUI`.
4. Choose UI building blocks instead of chasing a generic "pretty component library".
5. Define typography, layout rhythm, surface treatment, and a semantic color system.
6. Choose motion tooling only if native animation is not enough.
7. Return a compact build brief with explicit assumptions and one memorable signature idea.

## Discovery Questions

Ask only what will materially change the plan:

- What does the app do, and who is the primary user?
- Is this native iOS only, or is there real cross-platform pressure?
- Is this a greenfield app or an existing UIKit / Objective-C codebase?
- What are the main constraints: minimum iOS version, deadline, team experience, accessibility, design assets?
- What tone should the app feel like: trustworthy, calm, energetic, premium, playful, or minimal?
- What visual direction should the interface lean toward: editorial, glassy, tactile, clinical, sporty, luxurious, toy-like, or quiet utility?
- What should make the UI memorable after ten seconds of use: typography, cards, imagery, icon motion, depth, or a specific hero interaction?
- What motion is actually needed: none, subtle feedback, onboarding loops, interactive state machines, or shared-element transitions?

If the user omits an answer, make a reasonable assumption and label it explicitly.

## Stack Decision

- Default a new native iOS app to `Swift + SwiftUI`.
- Use `UIKit` when working inside an existing UIKit codebase, when heavy view-controller coordination is already present, or when UIKit-only transitions and imperative control are the main constraint.
- Use a hybrid approach when most screens can be SwiftUI but one or two features need UIKit escape hatches.
- Avoid `Objective-C` for new work unless the repository already depends on it.
- If the user explicitly needs one codebase for both iOS and Android, state that this becomes a product-stack decision outside the default native path; do not derail a native iOS brief unless the user asks.

Read [references/ios-decision-playbook.md](references/ios-decision-playbook.md) when the stack or UI helper choice is unclear.

## Art Direction

- Do not settle for "clean modern app" as a design direction. Name a stronger concept and execute it consistently.
- Pick one memorable signature element such as editorial type contrast, liquid-glass depth, oversized cards, diagram-like iconography, or a dramatic hero transition.
- Keep the interface native in interaction even when the visual language is bold.
- Use contrast intentionally: refined minimalism, athletic energy, calm clinical clarity, playful tactility, or premium instrument-panel precision can all work if the direction is coherent.

Read [references/ui-art-direction-playbook.md](references/ui-art-direction-playbook.md) when the user wants a better-looking UI but cannot describe the style precisely.

## Visual System

- Prefer Apple system components, `SF Symbols`, system materials, and custom design tokens over a heavy third-party UI kit.
- Treat "更漂亮" as a design-system problem: hierarchy, spacing, type scale, iconography, surfaces, and motion.
- Use focused libraries only to fill a specific gap. Do not add a dependency only because the UI feels plain.
- Preserve Apple ergonomics and accessibility while pushing the visual direction through composition and styling.

## Typography And Layout

- Use `SF Pro` as the default body typeface for product UI because it is the system font and designed for legibility on Apple platforms.
- Consider `New York` for reading-heavy, editorial, or premium display moments.
- Add a custom font only when it reinforces the concept and does not damage readability, localization, or Dynamic Type support.
- Define a visible type hierarchy, spacing rhythm, corner-radius family, and density model before polishing individual screens.
- Use asymmetry, overlap, section contrast, or spacious negative space when the concept calls for it, but keep navigation and touch targets predictable.

## Theme

- Pick one accent family, one neutral family, and explicit semantic colors.
- Always consider light mode, dark mode, contrast, and accessibility before locking the palette.
- Prefer system-defined or asset-catalog-driven colors that can adapt with the environment.
- Use backgrounds, materials, gradients, imagery, or texture only when they reinforce the concept; avoid flat default screens unless minimalism is the actual direction.
- Use `python3 scripts/generate_theme_tokens.py --mood trust` to get a starting palette, or pass `--accent HEX` after the brand direction is clear.

Read [references/theme-playbook.md](references/theme-playbook.md) for archetypes and token rules.

## Motion

- Start with native `SwiftUI` or `UIKit` animation APIs.
- Add `Lottie` only for designer-authored playback animations such as onboarding loops, celebratory states, or marketing-style motion.
- Add `Rive` only for interactive or stateful motion that responds to runtime inputs.
- Add `Hero` only for UIKit-heavy shared-element transitions.
- Respect `Reduce Motion` and avoid decorative motion in core task flows.
- Favor one or two high-impact motion moments over constant low-value animation noise.

Read [references/motion-playbook.md](references/motion-playbook.md) when choosing a motion library.

## Output Format

Return a short build brief with:

- Recommended stack
- Art direction and signature element
- UI component source and optional libraries
- Typography and layout rules
- Theme direction and semantic tokens
- Animation choice and why
- First implementation steps

## Example Brief

- Stack: `Swift + SwiftUI`, iOS 17+, add UIKit only for camera and share-sheet edge cases.
- Art direction: quiet premium dashboard with instrument-panel precision and one memorable glassy hero metric card.
- UI: system components, `SF Symbols`, custom design tokens, `Swift Charts` if dashboard views are needed.
- Typography: `SF Pro` for product text, `New York` for one editorial summary header, generous top spacing, large section breaks, and restrained radii.
- Theme: `trust` archetype with cool neutrals and cobalt accent, plus semantic success / warning / danger colors.
- Motion: native SwiftUI transitions for navigation and state changes; `Lottie` only if a designer provides exported onboarding animations.
- Next steps: sketch the information architecture, generate theme tokens, then scaffold the first two core screens in SwiftUI previews.
