'use client'
import { useState, useEffect } from "react"
import { handleStickyNav, handleBackToTop, handleTeamHover } from "@/lib/animation"
import HeroCard from "@/components/contents/HeroCard"
import AboutCard from "@/components/contents/AboutCard"
import HeaderSection from "@/components/layout/HeaderSection"
import FooterSection from "@/components/layout/FooterSection"
import FontLoadChecker from "@/components/FontLoadChecker"
import FontDemo from "@/components/contents/FontDemo"

export default function MainContent() {
  const [showSpinner, setShowSpinner] = useState(true)

  // Simulate page loading with spinner
  useEffect(() => {
    const timer = setTimeout(() => {
      setShowSpinner(false)
    }, 1000)

    return () => clearTimeout(timer)
  }, [])

  // Initialize animations and interactions
  useEffect(() => {
    if (!showSpinner) {
      // Use setTimeout to ensure DOM is fully loaded
      const animationTimeout = setTimeout(() => {
        // We can remove animateCounters() as we're now using the AnimatedCounter component
        handleStickyNav()
        handleBackToTop()
        handleTeamHover()
      }, 100)

      return () => clearTimeout(animationTimeout)
    }
  }, [showSpinner])

  return (
    <>
      <FontLoadChecker />
      <HeaderSection activeLink="home" />
      <main>
        {/* Spinner Card */}
        <HeroCard />
        {/* About Start */}
        <AboutCard />
        {/* About End */}

        {/* Font Demo Section - Remove this in production */}
        <div className="container-fluid p-5 bg-light">
          <FontDemo />
        </div>
      </main>
      <FooterSection />
    </>
  )
}