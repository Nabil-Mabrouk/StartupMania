/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "../../**/templates/**/*.html", // Django templates
      "../../**/static/js/**/*.js",  // JavaScript files in static
    ],
theme: {
    extend: {
        colors: {
            primary: {
                light: '#0466c8', // Light orange
                DEFAULT: '#0353a4', // Default orange
                dark: '#023e7d', // Dark orange
            },
        },
        animation: {
            'gradient-pulse': 'gradient-pulse 8s ease infinite',
            'float': 'float 12s ease-in-out infinite',
        },
        keyframes: {
            'gradient-pulse': {
                '0%, 100%': { opacity: '0.3' },
                '50%': { opacity: '0.5' },
            },
            'float': {
                '0%, 100%': { transform: 'translateY(0) translateX(0)' },
                '50%': { transform: 'translateY(-20px) translateX(10px)' },
            }
        }
    },
},
plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography')
],
};