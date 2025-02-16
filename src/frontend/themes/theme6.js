/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "../../**/templates/**/*.html", // Django templates
      "../../**/static/js/**/*.js",  // JavaScript files in static
    ],
    darkMode: 'class', // Dark mode support
    theme: {
      extend: {
              // Adding an SVG texture as a background image
      backgroundImage: {
        'cyberpunk-texture': "url('/static/landing/backgrounds/noise.webp')",
      },
      backgroundColor: {
        'overlay': 'rgb(13, 25, 39)', // Semi-transparent black overlay for better text visibility
      },
        colors: {
          // Theme colors with a modern tech feel
          primary: '#3B82F6', // Cool blue
          secondary: '#9333EA', // Vibrant purple
          background: '#F8FAFC', // Light neutral background
          text: '#111827', // Dark text for high contrast
          card: '#FFFFFF', // White cards for a clean look
          glass: 'rgba(255, 255, 255, 0.2)', // Subtle glassmorphism effect
          muted: '#6B7280', // Muted gray text
          error: '#EF4444', // Red for errors
          success: '#10B981', // Green for success
          warning: '#F59E0B', // Amber for warnings
          buttonHover: '#2563EB', // Slightly darker blue on hover
        },
        backdropBlur: {
          sm: '6px', // Increased blur for a more pronounced glass effect
          md: '12px',
        },
        boxShadow: {
          glow: '0 10px 40px rgba(0, 0, 0, 0.3)', // Softer glowing effect
          card: '0 4px 20px rgba(0, 0, 0, 0.15)', // Subtle shadow for cards
          button: '0 2px 12px rgba(59, 130, 246, 0.4)', // Glowing blue for buttons
          glass: '0 10px 30px rgba(0, 0, 0, 0.2)', // Glassmorphism glow
        },
        borderRadius: {
          lg: '20px', // Larger radius for modern cards and buttons
          xl: '30px', // Extra large radius for some unique elements
        },
        fontFamily: {
          body: ['Inter', 'sans-serif'], // Modern sans-serif for body
          heading: ['Poppins', 'sans-serif'], // Elegant heading font
        },
        spacing: {
          '18': '4.5rem',
          '22': '5.5rem',
          '28': '7rem', // More space for larger layouts
        },
        animation: {
          bounce: 'bounce 1.5s infinite', // Smoother bounce effect
          fadeIn: 'fadeIn 1s ease-out', // New fade-in animation for smooth transitions
          glow: 'glow 2s ease-in-out infinite', // Glowing effect for certain UI elements
        },
        keyframes: {
          bounce: {
            '0%, 100%': { transform: 'translateY(-10%)' },
            '50%': { transform: 'translateY(0)' },
          },
          fadeIn: {
            '0%': { opacity: 0 },
            '100%': { opacity: 1 },
          },
          glow: {
            '0%': { boxShadow: '0 0 20px rgba(59, 130, 246, 0.7)' },
            '50%': { boxShadow: '0 0 40px rgba(59, 130, 246, 0.9)' },
            '100%': { boxShadow: '0 0 20px rgba(59, 130, 246, 0.7)' },
          },
        },
        typography: {
          DEFAULT: {
            css: {
              color: '#111827',
              a: {
                color: '#3B82F6', // Primary link color
                '&:hover': {
                  color: '#9333EA', // Secondary link color on hover
                },
              },
              h1: {
                fontFamily: 'Poppins, sans-serif',
                fontWeight: '600',
                color: '#111827',
              },
              h2: {
                fontFamily: 'Poppins, sans-serif',
                fontWeight: '500',
                color: '#111827',
              },
              p: {
                lineHeight: '1.7',
              },
              blockquote: {
                fontStyle: 'italic',
                color: '#6B7280',
                borderLeft: '4px solid #9333EA',
                paddingLeft: '1rem',
              },
            },
          },
        },
        gradients: {
          // Soft gradient for buttons and backgrounds
          primary: 'linear-gradient(135deg, #3B82F6, #9333EA)',
          secondary: 'linear-gradient(135deg, #2563EB, #9333EA)',
        },
      },
    },
    plugins: [
      require('@tailwindcss/forms'), // For form styling
      require('@tailwindcss/typography'), // For typography styling
      require('@tailwindcss/aspect-ratio'), // Aspect ratio plugin for responsive images
      require('tailwindcss-gradients'), // Custom gradients plugin
    ],
  };
  