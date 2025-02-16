Prompt:
You are a frontend developer with expertise in Tailwind CSS and modern web design. Your task is to create highly aesthetic themes for a Django project by modifying or extending the values in the following Tailwind CSS configuration.

Requirements:
Preserve Structure: Do not remove any existing fields from the configuration. You can only change the values or add new fields to enhance the theme.
Aesthetic Standards:
Ensure visual harmony by choosing a cohesive color palette aligned with the theme’s purpose.
Typography should be legible and match the theme’s personality (e.g., modern, elegant, futuristic).
Use spacing, shadows, and borders to create a clean and balanced layout.
Incorporate modern design trends (e.g., gradients, glassmorphism, neumorphism) without overwhelming the design.
Accessibility:
Maintain high contrast between text and background for readability.
Ensure the theme is usable in both light and dark modes.
Modern Features:
Add vibrant effects like glowing borders, soft shadows, or subtle animations where appropriate.
Introduce fields for animations, gradients, or other Tailwind extensions to make the theme dynamic and visually engaging.
Theme Variation:
Create a theme with a clear, unique identity (e.g., a dark neon theme for gaming, a minimalist pastel theme for blogs, or a vibrant creative portfolio theme).
Usability:
Ensure the theme supports all core UI components: forms, cards, buttons, tables, lists, markdown, images, and navigation.
Starting Configuration (Template):
javascript
Copier le code
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../../**/templates/**/*.html", // Django templates
    "../../**/static/js/**/*.js",  // JavaScript files in static
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Theme colors
        primary: '#7F00FF', // Example: Deep purple
        secondary: '#E100FF', // Example: Neon pink
        background: '#F5F7FA', // Example: Light neutral
        text: '#333333', // Example: Dark text
        card: '#FFFFFF', // Example: White cards
        glass: 'rgba(255, 255, 255, 0.3)', // Example: Glass effect
        muted: '#6B7280', // Example: Gray muted text
        error: '#EF4444', // Example: Red for errors
        success: '#10B981', // Example: Green for success
        warning: '#F59E0B', // Example: Amber for warnings
        buttonHover: '#6000E6', // Example: Slightly darker primary
      },
      backdropBlur: {
        sm: '4px',
        md: '8px',
      },
      boxShadow: {
        glow: '0 4px 30px rgba(0, 0, 0, 0.5)',
        card: '0 2px 10px rgba(0, 0, 0, 0.1)',
        button: '0 2px 6px rgba(127, 0, 255, 0.5)',
      },
      borderRadius: {
        lg: '16px',
      },
      fontFamily: {
        body: ['Roboto', 'sans-serif'],
        heading: ['Oswald', 'sans-serif'],
      },
      spacing: {
        '18': '4.5rem',
        '22': '5.5rem',
      },
      animation: {
        bounce: 'bounce 1s infinite',
      },
      keyframes: {
        bounce: {
          '0%, 100%': { transform: 'translateY(-10%)' },
          '50%': { transform: 'translateY(0)' },
        },
      },
      typography: {
        DEFAULT: {
          css: {
            color: '#333333',
            a: {
              color: '#7F00FF',
              '&:hover': {
                color: '#E100FF',
              },
            },
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
};
Your Output:
Generate a complete, aesthetic theme configuration by modifying the above template. Ensure the following:

All fields are present.
The values align with the specified aesthetic goals.
Add fields where necessary to enhance the design (e.g., gradients, custom animations, advanced typography).
Example Themes:
1. Nature-Inspired Theme
Color-Scheme: Dark
Primary Color: "oklch(50% 0.4 120)" (A rich green reminiscent of lush forest foliage)
Secondary Color: "oklch(40% 0.3 210)" (A soft sky blue)
Accent Color: "oklch(80% 0.2 100)" (Earthy brown with warm tones)
Base Content: "oklch(12% 0.1 35)" (Muted, dark soil tone for background)
Info: "#6e91b1" (Gentle azure blue for highlighting important information)
Success: "#38b75c" (Vibrant green for positive actions or success)
Warning: "#d7a636" (Golden, warm yellow for attention)
Error: "#b93e44" (Crimson for error messages)
2. Sunset Beach Theme
Color-Scheme: Light
Primary Color: "oklch(60% 0.3 55)" (Soft coral pink)
Secondary Color: "oklch(72% 0.35 220)" (Lavender purple, creating contrast)
Accent Color: "oklch(90% 0.2 300)" (Golden orange like a sunset)
Neutral: "#f1e4b3" (Light sand for neutral tones)
Base-100: "oklch(100% 0 0)" (Bright white background)
Base-200: "#f9e1c4" (Sandy beige)
Base-300: "#faebd7" (Light cream for softer sections)
3. Cyberpunk Neon Glow
Color-Scheme: Dark
Primary Color: "oklch(50% 0.5 150)" (Neon cyan for high-tech appeal)
Secondary Color: "oklch(70% 0.45 120)" (Vibrant neon green for accent)
Accent Color: "oklch(55% 0.4 290)" (Electric purple for added futuristic vibe)
Neutral: "#1c1b1d" (Dark background with a slight purple tint)
Base-100: "#121212" (Pure black for dark mode)
Base-Content: "#e2e2e2" (Light gray for contrast)
Info: "#00b0ff" (Bright blue for informational elements)
Success: "#00e676" (Vivid green for success messages)
Error: "#d50000" (Bright red for errors)
4. Autumn Harvest Theme
Color-Scheme: Light
Primary Color: "#8C0327" (Deep red, inspired by fall leaves)
Secondary Color: "#D85251" (Rich orange for harvest vibes)
Accent Color: "#D59B6A" (Golden, earthy accents)
Neutral: "#826A5C" (Muted brown for calm background)
Base-100: "#f1f1f1" (Soft neutral for easy reading)
Info: "#42ADBB" (Aqua for highlighting important info)
Success: "#499380" (Earthy green for success signals)
Warning: "#E97F14" (Vibrant orange for warning messages)
Error: "oklch(53.07% 0.241 24.16)" (Rusty red for errors)
5. Luxury Opulence Theme
Color-Scheme: Dark
Primary Color: "oklch(100% 0 0)" (Pure black for luxury and elegance)
Secondary Color: "#152747" (Deep navy blue for richness)
Accent Color: "#513448" (Subtle burgundy accent)
Neutral: "#331800" (Dark brown, creating a high-end mood)
Neutral Content: "#FFE7A3" (Golden for content to pop against dark tones)
Base-100: "#09090b" (Black for deep dark background)
Base-200: "#171618" (Off black for secondary layers)
Base-Content: "#dca54c" (Golden highlights for sections)
6. Futuristic Neon Tech
Color-Scheme: Dark
Primary Color: "#e779c1" (Neon pink for a futuristic look)
Secondary Color: "#58c7f3" (Sky blue for accents)
Accent Color: "oklch(88.04% 0.206 93.72)" (Light purple with high contrast)
Neutral: "#221551" (Deep indigo background for a tech-inspired feel)
Neutral Content: "#f9f7fd" (Soft white for readability)
Base-100: "#1a103d" (A very dark purple background)
Base Content: "#f9f7fd" (White for content text)