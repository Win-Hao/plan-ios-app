# UI Art Direction Playbook

## Goal

Turn vague requests like "make it prettier" into a specific visual concept that can survive implementation.

## Design Thinking

Before naming components or libraries, decide:

- Purpose: what job does the app do, and what emotional posture should it take?
- Tone: pick a strong lane instead of a bland midpoint.
- Constraints: iOS version, accessibility, localization, team skill, timeline, and asset availability.
- Differentiation: what is the one thing a user will remember after using the app?

Do not stop at "modern" or "clean". Commit to a sharper point of view.

## Strong iOS-Friendly Directions

### Quiet Utility

- Best for productivity, admin, note-taking, and operational apps.
- Visual language: restrained palette, sharp hierarchy, compact information density, minimal decoration.
- Signature ideas: one bold metric strip, structured list rhythm, confident whitespace.

### Calm Clinical

- Best for health, mindfulness, habit, and education products.
- Visual language: soft surfaces, gentle spacing, warm or cool neutrals, low-stress motion.
- Signature ideas: breathing space, subtle translucency, reassuring cards.

### Athletic Pulse

- Best for fitness, delivery, event, and action-oriented products.
- Visual language: strong contrast, compressed headlines, fast motion, assertive accents.
- Signature ideas: oversized progress moments, energetic data views, kinetic icon transitions.

### Editorial Premium

- Best for media, reading, creator, travel, and luxury-oriented products.
- Visual language: stronger typographic personality, large image moments, curated spacing, selective serif usage.
- Signature ideas: magazine-like hero sections, display typography, quiet but rich surfaces.

### Playful Tactile

- Best for social, education, family, and youth-oriented products.
- Visual language: rounder shapes, clearer color separation, cheerful motion, slightly exaggerated hierarchy.
- Signature ideas: toy-like cards, expressive icons, lively confirmation states.

### Precision Glass

- Best for finance, dashboards, pro tools, and data-heavy experiences that still need drama.
- Visual language: layered surfaces, refined translucency, crisp dividers, luminous accents.
- Signature ideas: glass panels, focused depth, dashboard instrumentation.

## Typography Rules

- Default to `SF Pro` for most product UI because it is the iOS system font and optimized for legibility.
- Use `New York` for display or reading-heavy moments when the concept needs more editorial tone.
- Add a custom font only for a clear brand reason and only after checking readability, localization, and Dynamic Type behavior.
- Create contrast through weight, width, case, and size before importing more fonts.

## Composition Rules

- Use a clear density model: spacious, balanced, or compact.
- Introduce asymmetry, overlap, or hero sections only where they improve memorability.
- Keep core navigation and gesture expectations native even if the layout is bold.
- Use surfaces, materials, imagery, and texture in service of the concept, not as decoration by default.

## Motion Rules

- Pick one signature motion idea, such as staggered reveal, symbol morphing, card lift, or shared-element focus.
- Keep repeated UI interactions efficient and calm.
- Save heavier motion for onboarding, hero states, or delight moments.

## Output Shape

When using this playbook, return:

- Visual direction
- Signature element
- Typography system
- Layout rhythm
- Surface and background treatment
- Motion stance
- Risks to watch

## Source Links

- Reference frontend design skill: https://skillsmp.com/skills/anthropics-claude-code-plugins-frontend-design-skills-frontend-design-skill-md
- Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Designing for iOS: https://developer.apple.com/design/human-interface-guidelines/designing-for-ios
- Apple fonts: https://developer.apple.com/fonts/
- SF Symbols: https://developer.apple.com/sf-symbols/
