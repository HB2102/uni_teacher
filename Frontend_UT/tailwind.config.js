/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
    fontFamily: {
      iran: ['iran'], 
    },
    lineHeight: {
      'relaxed': '1.25',
    },
  },
  plugins: [
    () => import('tailwindcss-rtl')
  ],
  darkMode: "class",
}