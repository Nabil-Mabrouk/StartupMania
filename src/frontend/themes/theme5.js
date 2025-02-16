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
          primary: '#6A00FF', // Deep electric purple for a vibrant futuristic look
          secondary: '#00E5D3', // Bright teal that contrasts well with purple
          background: '#F9F9F9', // Light neutral background for light mode
          backgroundDark: '#1F1F1F', // Dark background for dark mode
          text: '#1A202C', // Dark text for clarity on light backgrounds
          textDark: '#F5F5F5', // Light text for dark mode
          card: '#FFFFFF', // White for clean, minimal cards
          glass: 'rgba(255, 255, 255, 0.15)', // Slightly opaque glass effect
          muted: '#A0AEC0', // Muted gray text for less emphasis
          error: '#F56565', // Soft red for errors
          success: '#38A169', // Green for success messages
          warning: '#DD6B20', // Warm amber for warnings
          buttonHover: '#5A00CC', // Darker purple for hover effect
          gradientStart: '#6A00FF', // Gradient start color
          gradientEnd: '#00E5D3', // Gradient end color
        },
        backdropBlur: {
          sm: '6px',
          md: '12px',
        },
        boxShadow: {
          glow: '0 4px 40px rgba(106, 0, 255, 0.5)', // Glowing effect for buttons/cards
          card: '0 4px 30px rgba(0, 0, 0, 0.1)', // Light shadow for cards
          button: '0 4px 12px rgba(106, 0, 255, 0.3)', // Subtle button shadow
          focus: '0 0 8px rgba(106, 0, 255, 0.7)', // Focus state glow
        },
        borderRadius: {
          lg: '16px',
          full: '9999px', // For round elements like buttons
        },
        fontFamily: {
          body: ['Inter', 'sans-serif'], // Modern sans-serif for readability
          heading: ['Poppins', 'sans-serif'], // Bold, geometric font for headings
        },
        spacing: {
          '18': '4.5rem',
          '22': '5.5rem',
          '24': '6rem', // Extra spacing for larger elements
        },
        animation: {
          fadeIn: 'fadeIn 1s ease-out', // Subtle fade-in animation
          bounce: 'bounce 1s infinite', // Bouncy animation for interactive elements
          glow: 'glow 1.5s ease-in-out infinite', // Glowing animation for neon effects
        },
        keyframes: {
          fadeIn: {
            '0%': { opacity: '0' },
            '100%': { opacity: '1' },
          },
          bounce: {
            '0%, 100%': { transform: 'translateY(-10%)' },
            '50%': { transform: 'translateY(0)' },
          },
          glow: {
            '0%': { textShadow: '0 0 5px rgba(106, 0, 255, 0.7)' },
            '50%': { textShadow: '0 0 10px rgba(106, 0, 255, 1)' },
            '100%': { textShadow: '0 0 5px rgba(106, 0, 255, 0.7)' },
          },
        },
        typography: {
          DEFAULT: {
            css: {
              color: '#1A202C',
              a: {
                color: '#6A00FF',
                '&:hover': {
                  color: '#00E5D3',
                },
              },
              h1: {
                fontFamily: 'Poppins, sans-serif',
                fontWeight: '700',
                color: '#1A202C',
              },
              h2: {
                fontFamily: 'Poppins, sans-serif',
                fontWeight: '600',
                color: '#1A202C',
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
  