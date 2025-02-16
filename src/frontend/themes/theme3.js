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
        // Electric Neon theme colors
        primary: '#00FFFF', // Cyan
        secondary: '#FF00FF', // Neon Magenta
        background: '#0F0F1E', // Deep dark background
        text: '#E0E0E0', // Soft white
        card: '#1C1C2D', // Dark card background
        glass: 'rgba(0, 0, 0, 0.5)', // Dark semi-transparent glass effect
        muted: '#828282', // Neutral muted text
        error: '#FF3333', // Bright red
        success: '#33FF99', // Bright green
        warning: '#FF9900', // Vibrant orange
        buttonHover: '#00E5FF', // Electric cyan for hover
      },
      backdropBlur: {
        sm: '6px', // Medium blur for glass effect
        md: '12px', // Stronger blur
      },
      boxShadow: {
        glow: '0 4px 20px rgba(0, 255, 255, 0.7)', // Cyan neon glow
        card: '0 2px 15px rgba(255, 0, 255, 0.4)', // Magenta glow
        button: '0 4px 15px rgba(0, 255, 255, 0.6)', // Cyan button shadow
      },
      borderRadius: {
        lg: '16px', // Larger radius for futuristic feel
      },
      fontFamily: {
        body: ['Source Code Pro', 'monospace'], // High-tech font
        heading: ['Orbitron', 'sans-serif'], // Futuristic geometric font
      },
      spacing: {
        '18': '4.5rem', // Standard spacing
        '22': '5.5rem',
      },
      animation: {
        pulse: 'pulse 1.5s infinite', // Electric pulse effect
      },
      keyframes: {
        pulse: {
          '0%, 100%': { opacity: '1', transform: 'scale(1)' },
          '50%': { opacity: '0.7', transform: 'scale(1.05)' },
        },
      },
      typography: {
        DEFAULT: {
          css: {
            color: '#E0E0E0',
            a: {
              color: '#00FFFF',
              '&:hover': {
                color: '#FF00FF',
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
