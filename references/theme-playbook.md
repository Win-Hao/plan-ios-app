# Theme Playbook

## Gather Inputs First

Ask for:

- App category
- Primary audience
- Brand tone in two or three adjectives
- Whether the UI should feel dense and efficient or open and emotional
- Whether the app must feel more trustworthy, calm, energetic, premium, playful, or minimal
- Whether the app should feel editorial, glassy, tactile, sporty, clinical, or quiet

## Fast Archetypes

| Archetype | Good fit | Accent direction | Neutral direction | Notes |
| --- | --- | --- | --- | --- |
| `trust` | finance, admin, B2B, health data | cobalt, blue, teal-blue | cool gray, slate | Stable and credible |
| `calm` | wellness, journaling, sleep, focus | teal, mint, soft green | warm gray, soft stone | Low stress and restorative |
| `energetic` | fitness, commerce, delivery, events | orange, coral | warm neutrals | Fast and active |
| `premium` | pro tools, luxury, creator apps | deep emerald, deep cobalt | graphite, warm stone | Restrained saturation |
| `playful` | kids, social, education, casual | coral, pink-orange, bright blue | soft cool gray | More contrast and shape |
| `minimal` | utilities, productivity, note apps | blue, teal, neutral black | cool gray | Quiet and content-first |

## Semantic Token Rules

Define semantic roles instead of painting every screen ad hoc:

- `background`
- `surface`
- `surfaceElevated`
- `textPrimary`
- `textSecondary`
- `border`
- `accent`
- `accentSoft`
- `success`
- `warning`
- `danger`

Keep one main accent. Do not use three competing brand colors unless the product truly needs a vivid multi-brand look.

## Surface And Atmosphere Rules

- Decide whether the app wants flat restraint, soft material depth, strong card separation, immersive gradients, or image-led storytelling.
- Use one atmosphere system consistently instead of mixing heavy shadows, random gradients, and unrelated glass effects.
- On iOS, bold visuals should still preserve legibility, touch clarity, and content hierarchy.

## Light And Dark Rules

- Keep the accent hue consistent across modes.
- Make dark mode accents slightly brighter so they do not die on dark surfaces.
- Use separate semantic colors for status instead of recoloring the main accent for every state.
- Prefer colors that can adapt through asset catalogs or system dynamic colors.

## Accessibility Rules

- Check contrast for text and iconography on every branded surface.
- Convey meaning with icons, labels, or shape in addition to color.
- Prefer system-defined colors when possible because they adapt to accessibility settings.
- Re-check the palette with Dynamic Type and darker backgrounds before calling it finished.

## Using The Palette Script

Generate a starting point:

```bash
python3 scripts/generate_theme_tokens.py --mood trust
```

Override the accent and output JSON:

```bash
python3 scripts/generate_theme_tokens.py --accent 2E6BFF --neutral cool --format json
```

Write to a file:

```bash
python3 scripts/generate_theme_tokens.py --mood calm --output theme-tokens.json --format json
```

Treat the script output as a draft. Adjust after looking at real screens, not in isolation.

## Source Links

- Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Accessibility guidance: https://developer.apple.com/design/human-interface-guidelines/accessibility
- Designing for iOS: https://developer.apple.com/design/human-interface-guidelines/designing-for-ios
- System colors: https://developer.apple.com/documentation/uikit/standard-colors
- UIColor overview: https://developer.apple.com/documentation/uikit/uicolor
