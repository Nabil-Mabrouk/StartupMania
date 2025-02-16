module.exports = {
    content: [
        "../../**/templates/**/*.html", // Django templates
        "../../**/static/js/**/*.js",  // JavaScript files in static
      ],
    theme: {
      extend: {
        // Color Palette
        colors: {
          primary: {
            DEFAULT: '#3B82F6', // blue-500
            400: '#60A5FA',      // blue-400
            600: '#2563EB'       // blue-600
          },
          secondary: {
            DEFAULT: '#8B5CF6', // purple-500
            400: '#A78BFA'      // purple-400
          },
          dark: {
            base: '#030712',     // gray-950
            800: '#1F2937',      // gray-800
            900: '#111827'       // gray-900
          },
          accent: {
            blue: {
              200: '#BFDBFE',    // blue-200
              300: '#93C5FD'     // blue-300
            },
            purple: {
              300: '#C4B5FD'     // purple-300
            }
          }
        },
  
        // Gradient Configuration
        gradientColorStops: theme => ({
          'primary-gradient': `linear-gradient(45deg, ${theme('colors.primary.400')}, ${theme('colors.secondary.400')})`,
          'dark-gradient': `linear-gradient(45deg, ${theme('colors.dark.base')}, ${theme('colors.dark.base')} 50%, ${theme('colors.dark.900')})`
        }),
  
        // Animation Configuration
        animation: {
          'gradient-pulse': 'gradient-pulse 8s ease infinite',
          'gradient-underline': 'gradient-underline 0.5s ease forwards',
          'float': 'float 12s ease-in-out infinite'
        },
        keyframes: {
          'gradient-pulse': {
            '0%, 100%': { opacity: '0.3' },
            '50%': { opacity: '0.5' }
          },
          'gradient-underline': {
            '0%': { backgroundSize: '0% 2px' },
            '100%': { backgroundSize: '100% 2px' }
          },
          'float': {
            '0%, 100%': { transform: 'translateY(0) translateX(0)' },
            '50%': { transform: 'translateY(-20px) translateX(10px)' }
          }
        },
  
        // Border Configuration
        borderColor: theme => ({
          DEFAULT: theme('colors.dark.800'),
          'accent': 'rgba(96, 165, 250, 0.3)' // blue-400/30
        }),
  
        // Typography Configuration (for prose)
        typography: (theme) => ({
          DEFAULT: {
            css: {
              color: theme('colors.accent.blue.200'),
              '--tw-prose-headings': theme('colors.accent.blue.300'),
              '--tw-prose-links': theme('colors.primary.400'),
              '--tw-prose-pre-code': theme('colors.dark.900')
            }
          }
        })
      }
    },
    plugins: [
      require('@tailwindcss/typography'),
      require('@tailwindcss/forms'),
      // Custom plugin for gradient underlines
      function({ addUtilities }) {
        const newUtilities = {
          '.gradient-underline': {
            backgroundImage: `linear-gradient(45deg, ${this.theme('colors.primary.400')}, ${this.theme('colors.secondary.400')})`,
            backgroundSize: '0% 2px',
            backgroundPosition: 'left bottom',
            backgroundRepeat: 'no-repeat',
            transition: 'background-size 0.3s ease'
          },
          '.gradient-underline-hover': {
            backgroundSize: '100% 2px'
          }
        }
        addUtilities(newUtilities, ['hover'])
      }
    ]
  }