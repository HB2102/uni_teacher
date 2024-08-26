/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        iran: ['iran'], 
      },
      colors: {
        myNewColor: {
          DEFAULT: '#3498db',
          light: '#2980b9',
          dark: '#34495e',
        },}
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