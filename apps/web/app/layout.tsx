// app/layout.tsx
import { ThemeProvider } from "@/components/theme-provider"
import { Oswald, Rubik } from 'next/font/google';
import BackToTop from "@/components/layout/Backtotop";
import "./globals.css";
import "./chef.css";
import "./chef-extras.css";
import "../styles/header.css";
import "./fonts.css";

const oswald = Oswald({
  subsets: ['latin'],
  weight: ['400', '500', '600', '700'],
  variable: '--font-oswald',
});

const rubik = Rubik({
  subsets: ['latin'],
  weight: ['300', '400', '500', '600', '700'],
  variable: '--font-rubik',
});

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning className={`${oswald.variable} ${rubik.variable}`}>
      <body>
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          {children}
          <BackToTop />
        </ThemeProvider>
      </body>
    </html>
  )
}