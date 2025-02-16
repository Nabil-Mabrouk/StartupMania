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
          // Primary theme colors
          primary: '#1F2937', // Dark gray
          secondary: '#3B82F6', // Blue
          background: '#F3F4F6', // Light gray
          text: '#111827', // Dark text
          card: '#FFFFFF', // White cards
          glass: 'rgba(255, 255, 255, 0.3)', // Transparent glass effect
          muted: '#6B7280', // Gray muted text
          error: '#EF4444', // Red for errors
          success: '#10B981', // Green for success
          warning: '#F59E0B', // Amber for warnings
          buttonHover: '#2563EB', // Slightly darker shade of blue
        },
        backdropBlur: {
          sm: '4px',
          md: '8px',
        },
        boxShadow: {
          glow: '0 4px 30px rgba(0, 0, 0, 0.5)',
          card: '0 2px 10px rgba(0, 0, 0, 0.1)',
          button: '0 2px 6px rgba(59, 130, 246, 0.5)',
        },
        borderRadius: {
          lg: '16px',
        },
        fontFamily: {
          body: ['Inter', 'sans-serif'],
          heading: ['Poppins', 'sans-serif'],
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
              color: '#111827',
              a: {
                color: '#3B82F6',
                '&:hover': {
                  color: '#2563EB',
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
  