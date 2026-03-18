# iOS Stack And UI Decision Playbook

## Default Choices

- Language: use `Swift` for new native iOS work.
- UI layer: use `SwiftUI` for greenfield work unless a concrete constraint points elsewhere.
- Icons: use `SF Symbols` first.
- Design references: use Apple `Human Interface Guidelines` and Apple `Design Resources` before searching for a third-party design system.
- Distinctiveness: create it through art direction, typography, composition, materials, and motion before reaching for large UI kits.

## SwiftUI vs UIKit

### Use SwiftUI when

- The app is greenfield.
- The team wants faster iteration, previews, and less boilerplate.
- Most UI can be expressed declaratively.
- The app benefits from sharing patterns across Apple platforms later.

### Use UIKit when

- The project already has a large UIKit codebase.
- The app depends on view-controller-driven flows or highly customized collection / navigation behavior that already exists in UIKit.
- A third-party SDK only exposes UIKit views or controllers in a way that would make a SwiftUI wrapper awkward.

### Use a hybrid when

- Most new screens are simple in `SwiftUI`, but one or two areas need UIKit integration.
- The team wants to modernize incrementally instead of rewriting the whole app.

## How To Answer "What language should I use?"

- Native iOS only: answer `Swift`.
- Existing Objective-C app: add new code in `Swift` unless interoperability or build constraints force otherwise.
- Real iOS + Android single-codebase requirement: state clearly that `React Native` or `Flutter` changes the tradeoff, and do not pretend a native iOS recommendation solves that requirement.

## How To Answer "What component library should I use?"

- Default answer: do not start with a monolithic component library.
- Explain that iOS already ships the core design language through system components, typography, materials, haptics, and iconography.
- Recommend system components first: `NavigationStack`, `TabView`, `List`, `Form`, `ScrollView`, `Sheet`, `Toolbar`, `Menu`, `Alert`, `Gauge`, `ProgressView`.
- Recommend focused Apple frameworks for feature-specific UI:
  - `Swift Charts` for dashboards and metrics
  - `MapKit` for map-heavy apps
  - `PhotosUI` for media picking

## Focused Helpers Instead Of Heavy UI Kits

- `SwiftUI Introspect`: use sparingly when SwiftUI does not expose the UIKit or AppKit control you need.
- `SwiftUIX`: use only when a missing SwiftUI-like component is blocking the build.
- Build a small internal design-token layer instead of importing many visual dependencies.

## Beauty Checklist

- Name a specific art direction instead of asking for a generic modern UI.
- Pick one memorable signature element.
- Tighten hierarchy before adding libraries.
- Use a clear type scale and spacing rhythm.
- Choose a density model: airy, balanced, or compact.
- Use consistent spacing and corner radii.
- Limit accent colors.
- Decide whether the app relies on flat surfaces, cards, materials, or image-led sections.
- Use `SF Symbols` consistently before importing custom icon packs.
- Preview key screens in light mode, dark mode, and larger text sizes.

## Source Links

- SwiftUI overview: https://developer.apple.com/swiftui/
- UIKit overview: https://developer.apple.com/documentation/uikit
- SwiftUI pathway: https://developer.apple.com/pathways/swiftui/
- Human Interface Guidelines: https://developer.apple.com/design/human-interface-guidelines/
- Designing for iOS: https://developer.apple.com/design/human-interface-guidelines/designing-for-ios
- Apple Design Resources: https://developer.apple.com/design/
- SF Symbols: https://developer.apple.com/sf-symbols/
- SwiftUI Introspect: https://github.com/siteline/swiftui-introspect
- SwiftUIX: https://github.com/SwiftUIX/SwiftUIX
