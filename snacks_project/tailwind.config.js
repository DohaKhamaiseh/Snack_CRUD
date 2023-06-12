/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/home.html", "./templates/about.html"
   
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter var', ...defaultTheme.fontFamily.sans],
    },
  },
  plugins: [],
}

}