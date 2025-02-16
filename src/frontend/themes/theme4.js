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
          // Vibrant dark mode colors
          primary: '#00FFAB', // Vibrant neon green
          secondary: '#FF007F', // Neon pink
          background: '#1A1A2E', // Rich dark blue
          text: '#EAEAEA', // Light text for contrast
          card: '#222831', // Slightly lighter dark for cards
          glass: 'rgba(34, 40, 49, 0.7)', // Semi-transparent glass effect
          muted: '#7F8C8D', // Soft gray-muted text
          error: '#FF4C4C', // Bright red
          success: '#00D98B', // Bright aqua-green
          warning: '#FFC300', // Neon yellow
          buttonHover: '#12E2A3', // Brighter green hover
        },
        backdropBlur: {
          sm: '8px', // Enhanced glass effect
          md: '16px',
        },
        boxShadow: {
          glow: '0 0 20px rgba(0, 255, 171, 0.8)', // Green neon glow
          card: '0 4px 15px rgba(255, 0, 127, 0.5)', // Pink neon glow
          button: '0 4px 10px rgba(0, 255, 171, 0.6)', // Neon green button glow
        },
        borderRadius: {
          lg: '12px', // Rounded but sharp
          full: '9999px', // Pill shape for buttons
        },
        fontFamily: {
          body: ['Nunito Sans', 'sans-serif'], // Clean and readable
          heading: ['Exo', 'sans-serif'], // Futuristic, bold font
        },
        spacing: {
          '18': '4.5rem',
          '22': '5.5rem',
        },
        animation: {
          glowPulse: 'glowPulse 1.8s infinite', // Gentle neon pulsing
        },
        keyframes: {
          glowPulse: {
            '0%, 100%': { boxShadow: '0 0 15px rgba(0, 255, 171, 0.5)' },
            '50%': { boxShadow: '0 0 25px rgba(0, 255, 171, 0.8)' },
          },
        },
        typography: {
          DEFAULT: {
            css: {
              color: '#EAEAEA',
              a: {
                color: '#00FFAB',
                '&:hover': {
                  color: '#FF007F',
                },
              },
              h1: {
                color: '#00FFAB',
              },
              h2: {
                color: '#FF007F',
              },
              blockquote: {
                borderLeftColor: '#FF007F',
                color: '#EAEAEA',
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
  