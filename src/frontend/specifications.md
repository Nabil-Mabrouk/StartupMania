# Frontend Design System Specification  
**Project: Startup Mania**  
**Version: 1.0**

## 1. Core Design Principles
- **Dark Theme First**  
- **Gradient Emphasis** (Blue → Purple)  
- **Depth & Dimension** (Layered shadows)  
- **Motion** (300ms transitions)  
- **4px Base Unit** for spacing/sizing

## 2. Color Palette
| Category          | Tailwind Classes                                 |
|--------------------|-------------------------------------------------|
| Primary Gradient   | `from-blue-400` to `to-purple-400`              |
| Secondary Gradient | `from-gray-800` to `to-blue-900/20`             |
| Success Gradient   | `from-green-400` to `to-cyan-400`               |
| Text               | `text-white`, `text-blue-200/80`                |
| Backgrounds        | `bg-gray-800`, `bg-blue-900/20`                 |
| Borders            | `border-blue-800/30` → `hover:border-blue-700/50` |

## 3. Typography
```html
<!-- Headings -->
<h1 class="text-3xl md:text-4xl font-bold bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">

<!-- Body -->
<p class="text-lg text-blue-200/80">
```

## 4. Layout Structure
``` html
<section class="text-white min-h-screen flex items-center">
  <div class="container mx-auto px-4">
    <div class="max-w-3xl mx-auto text-center mb-12">
      <!-- Content -->
    </div>
  </div>
</section>
```
## 5. Components
### Buttons
``` html
<!-- Primary -->
<button class="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-400...">

<!-- Secondary -->
<button class="bg-gradient-to-r from-gray-600 to-gray-700...">

<!-- Success -->
<button class="bg-gradient-to-r from-green-500 to-cyan-600...">
```

### Form Elements
```html
<!-- Input -->
<input class="w-full px-4 py-3 rounded-lg bg-blue-900/20 border border-blue-800/30...">

<!-- Checkbox Cards -->
<label class="flex items-center space-x-3 p-4 bg-blue-900/20 rounded-lg border...">
```
## 6. Responsive Design

- Grid: grid gap-3 md:grid-cols-2
- Text Scaling: (text-3xl md:text-4xl) (text-lg md:text-xl)

## 7. Transitions & Animations

```css
transition-all duration-300 /* Base transition */
hover:scale-[1.02] /* Button hover effect */
focus:ring-4 focus:ring-color/20 /* Focus states */
border hover:border-color/50 /* Border transitions */
```

## 8. Custom Utilities
```html
<!-- Gradient Text -->
<div class="bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">

<!-- Custom Opacity Borders -->
<div class="border border-blue-800/30 hover:border-blue-700/50">

<!-- Form Helpers -->
{{ field|add_class:"your-tailwind-classes" }}
```

9. Error States (Example)
```html

<div class="text-red-400 text-sm mt-2 flex items-center">
  <svg class="w-4 h-4 mr-1">...</svg>
  {{ error }}
</div>
```

## 10. Documentation Requirements
- All pages must extend landing/base.html
- Use {% load form_helpers %}
- Maintain 4:5 vertical rhythm in content sections
- Maintain 30% background opacity
- All interactive elements must have hover/focus states
-  Use {% load form_helpers %} for consistent form styling

**Implementation Notes:**

- Ensure Tailwind config includes extended color palette
- All gradients must use bg-clip-text for text elements
- Maintain 30% opacity for background overlays
- Use transform-gpu for hardware-accelerated animations