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
          primary: 'oklch(50% 0.5 150)', // Neon cyan
          secondary: 'oklch(70% 0.45 120)', // Neon green
          accent: 'oklch(55% 0.4 290)', // Electric purple
          background: '#1c1b1d', // Dark background with slight purple tint
          base100: '#121212', // Pure black for dark mode
          baseContent: '#e2e2e2', // Light gray for contrast
          info: '#00b0ff', // Bright blue for informational elements
          success: '#00e676', // Vibrant green for success
          warning: '#ff8000', // Neon orange for warning
          error: '#ff4c4c', // Bright red for errors
          card: 'rgba(255, 255, 255, 0.1)', // Semi-transparent white for cards
          muted: '#6b7280', // Muted gray text
          glass: 'rgba(255, 255, 255, 0.3)', // Glass effect
          buttonHover: 'oklch(50% 0.5 170)', // Lighter neon cyan for button hover
        },
        backdropBlur: {
          sm: '4px',
          md: '8px',
          lg: '12px',
        },
        boxShadow: {
          glow: '0 4px 30px rgba(0, 255, 255, 0.5)', // Glowing neon cyan
          card: '0 2px 10px rgba(0, 0, 0, 0.2)', // Soft shadow for cards
          button: '0 2px 6px rgba(39, 255, 20, 0.4)', // Glowing shadow for buttons
        },
        borderRadius: {
          lg: '16px',
          full: '9999px', // For round buttons or icons
        },
        fontFamily: {
          body: ['Roboto', 'sans-serif'],
          heading: ['Orbitron', 'sans-serif'],
        },
        spacing: {
          '18': '4.5rem',
          '22': '5.5rem',
        },
        animation: {
          bounce: 'bounce 1s infinite',
          pulseGlow: 'pulseGlow 2s infinite', // Custom glowing effect for buttons
        },
        keyframes: {
          bounce: {
            '0%, 100%': { transform: 'translateY(-10%)' },
            '50%': { transform: 'translateY(0)' },
          },
          pulseGlow: {
            '0%': { boxShadow: '0 0 10px rgba(0, 255, 255, 0.8)' },
            '50%': { boxShadow: '0 0 20px rgba(0, 255, 255, 1)' },
            '100%': { boxShadow: '0 0 10px rgba(0, 255, 255, 0.8)' },
          },
        },
        typography: {
          DEFAULT: {
            css: {
              color: '#e2e2e2', // Light text color
              a: {
                color: '#00FFFF', // Cyan for links
                '&:hover': {
                  color: '#00b0ff', // Bright blue on hover
                },
              },
              h1: {
                fontSize: '3rem', // Large heading for impact
                fontFamily: 'Orbitron, sans-serif',
                color: '#00b0ff',
              },
              h2: {
                fontSize: '2rem',
                fontFamily: 'Orbitron, sans-serif',
                color: '#ff8000', // Neon orange
              },
            },
          },
        },
        gradients: {
          'neon': 'linear-gradient(135deg, rgba(0, 255, 255, 1) 0%, rgba(39, 255, 20, 1) 100%)',
        },
      },
    },
    plugins: [
      require('@tailwindcss/forms'),
      require('@tailwindcss/typography'),
    ],
  };
  