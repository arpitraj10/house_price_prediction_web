/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#2563eb", // blue-600
        secondary: "#16a34a", // green-600
      },
      borderRadius: {
        xl: "1rem",
      },
    },
  },
  plugins: [],
};
