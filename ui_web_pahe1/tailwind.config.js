/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./front-end/public/**/*.{html,js}"],
  theme: {
    colors:{
      "transparent":"transparent",
      "white": "#ffffff",
      "black": "#101316",
      "blue": "#1C4E8E",
      "light-gray":"#101316",
      "bg-gray" : "#A5A9AC",
      
    },
    container: {
      center: true,
      padding: {
        DEFAULT: '2rem',
        sm: '2rem',
        lg: '2rem',
        xl: '5rem',
        '2xl': '8rem',
      },
    },
    extend: {},
  },
  plugins:
    ["tailwindcss ,autoprefixer"]
  ,
}