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
        // Minimalistic theme colors
        primary: '#4A5568', // Slate gray
        secondary: '#2D3748', // Charcoal
        background: '#F7FAFC', // Very light gray
        text: '#1A202C', // Almost black
        card: '#FFFFFF', // White cards
        glass: 'rgba(255, 255, 255, 0.2)', // Subtle transparency
        muted: '#A0AEC0', // Cool gray muted text
        error: '#E53E3E', // Muted red
        success: '#38A169', // Muted green
        warning: '#DD6B20', // Muted amber
        buttonHover: '#4C51BF', // Muted deep blue
      },
      backdropBlur: {
        sm: '2px', // Softer blur
        md: '6px',
      },
      boxShadow: {
        glow: '0 4px 15px rgba(0, 0, 0, 0.3)', // Softer glow
        card: '0 1px 5px rgba(0, 0, 0, 0.05)', // Minimal shadow
        button: '0 1px 3px rgba(0, 0, 0, 0.2)', // Subtle button shadow
      },
      borderRadius: {
        lg: '8px', // Slightly smaller rounded corners
      },
      fontFamily: {
        body: ['Inter', 'sans-serif'], // Clean, modern font
        heading: ['Poppins', 'sans-serif'], // Elegant sans-serif
      },
      spacing: {
        '18': '4rem', // Reduced spacing
        '22': '5rem',
      },
      animation: {
        bounce: 'bounce 1.2s infinite', // Slower bounce
      },
      keyframes: {
        bounce: {
          '0%, 100%': { transform: 'translateY(-5%)' },
          '50%': { transform: 'translateY(0)' },
        },
      },
      typography: {
        DEFAULT: {
          css: {
            color: '#1A202C',
            a: {
              color: '#4A5568',
              '&:hover': {
                color: '#2D3748',
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

  