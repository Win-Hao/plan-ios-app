# plan-ios-app

`plan-ios-app` is a skill for planning native iOS apps before implementation starts.

It helps turn vague requests like "What language should I use?", "Which UI library will make it look better?", or "How should I choose colors and animation?" into a concrete build brief.

## What This Skill Does

This skill guides an agent to:

- choose the default stack for a new iOS app, with a bias toward `Swift + SwiftUI`
- decide when `UIKit` or a hybrid approach is the better fit
- shape a stronger UI art direction instead of settling for a generic "clean modern app"
- choose system components and focused helpers instead of heavy UI kits
- define typography, layout rhythm, surface treatment, and semantic color tokens
- pick the right animation approach: native motion, `Lottie`, `Rive`, or `Hero`

## Best For

Use this skill when:

- you are starting a new iOS app and do not know where to begin
- you need help choosing between `SwiftUI` and `UIKit`
- your app feels visually weak and needs clearer design direction
- you do not know how to choose theme colors or motion
- you want a compact iOS build brief before writing production code

## What The Output Looks Like

The skill returns a concise plan with:

- recommended stack
- UI art direction and signature element
- component source and optional libraries
- typography and layout rules
- theme direction and semantic color tokens
- animation choice and rationale
- first implementation steps

## Example Prompts

```text
Use $plan-ios-app to plan a habit tracker for young professionals. I want it to feel calm, premium, and more distinctive than a typical utility app.
```

```text
Use $plan-ios-app to choose the stack, visual direction, colors, and animation approach for a finance dashboard app aimed at first-time investors.
```

```text
Use $plan-ios-app to help me decide whether my new app should use SwiftUI or UIKit, and give me a UI direction that feels athletic and energetic.
```

## Repository Structure

- `SKILL.md`: main workflow and decision rules
- `agents/openai.yaml`: UI metadata for the skill
- `references/ios-decision-playbook.md`: stack and component decision guide
- `references/ui-art-direction-playbook.md`: visual direction guide
- `references/theme-playbook.md`: palette and semantic token guide
- `references/motion-playbook.md`: motion and animation guide
- `scripts/generate_theme_tokens.py`: helper script for generating starter color tokens

## Notes

- The skill is designed for native iOS planning first. If a real cross-platform requirement exists, it explicitly calls that out instead of hiding the tradeoff.
- The design guidance pushes for more distinctive UI, but keeps interaction behavior grounded in Apple platform conventions.
- The generated theme tokens are a starting point. They should still be reviewed on real screens in light mode, dark mode, and larger text sizes.
