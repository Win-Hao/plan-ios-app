# Motion Playbook

## Choose The Lowest-Complexity Option That Solves The Need

Start with the platform. Only add a library when the motion requirement is real.

## Native SwiftUI Or UIKit

Use native animation first when:

- The app only needs state transitions, microinteractions, loading feedback, sheet transitions, or scroll-linked polish.
- The team wants the least dependency risk.
- The app is `SwiftUI`-first.

Prefer native APIs for buttons, lists, sheets, tab changes, state changes, and simple matched transitions.

## Lottie

Use `Lottie` when:

- A designer provides exported animation assets.
- The animation is mostly playback, looping, or scrubbing.
- You need onboarding, empty states, success states, or promotional motion quickly.

Avoid `Lottie` when:

- The motion must react deeply to live app state.
- The team does not have a design pipeline that can produce clean Lottie assets.

Notes:

- Prefer the lightweight `lottie-spm` package path when integrating through Swift Package Manager.
- Recent versions support SwiftUI wrappers, but treat Lottie as a focused asset player, not as your whole motion system.

## Rive

Use `Rive` when:

- The animation must react to runtime state or user input.
- The design calls for state machines, parameterized characters, or interactive illustrations.
- The team is willing to manage `.riv` assets and runtime version compatibility.

Avoid `Rive` when:

- Native motion or Lottie is already enough.
- The team has no Rive design workflow.

Notes:

- The Apple runtime is Swift-first and available through Swift Package Manager.
- Use it for interactive graphics, not for every small transition.

## Hero

Use `Hero` when:

- The app is UIKit-heavy.
- You need view-controller shared-element or "magic move" style transitions.

Avoid `Hero` when:

- The app is mainly `SwiftUI`.
- Native transitions already cover the use case.

## Motion Rules

- Respect `Reduce Motion`.
- Animate state changes that help comprehension, not every object on screen.
- Keep durations short for frequent interactions.
- Pair key state confirmations with haptics when appropriate.
- Test motion on low-end devices and long lists before committing to a library.

## Source Links

- SwiftUI overview: https://developer.apple.com/swiftui/
- UIKit animation and haptics entry point: https://developer.apple.com/documentation/uikit
- Lottie for iOS: https://github.com/airbnb/lottie-ios
- Lottie SPM package: https://github.com/airbnb/lottie-spm
- Rive Apple runtime: https://rive.app/docs/runtimes/apple
- Rive runtime overview: https://rive.app/docs/runtimes
- Hero: https://github.com/HeroTransitions/Hero
