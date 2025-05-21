'use client'
import { useState, useEffect } from "react"
import { handleStickyNav, handleBackToTop, handleTeamHover } from "@/lib/animation"
import HeroCard from "@/components/contents/HeroCard"
import AboutCard from "@/components/contents/AboutCard"
import Facts from "@/components/contents/Facts"

export default function HomePage() {
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
    <main>
      {/* Spinner Card */}
      <HeroCard />
      {/* About Start */}
      <AboutCard />
      {/* About End */}
      {/* Facts Start */}
      <Facts />
    </main>
  )
}