'use client'
import React, { useState, useEffect } from "react"

interface CounterProps {
    end: number;
    duration?: number;
    prefix?: string;
    suffix?: string;
}

export function AnimatedCounter({ end, duration = 2000, prefix = '', suffix = '' }: CounterProps) {
    const [count, setCount] = useState(0)

    useEffect(() => {
        if (count < end) {
            const increment = Math.ceil(end / (duration / 15))
            const timer = setTimeout(() => {
                setCount(prev => {
                    const newCount = prev + increment
                    return newCount >= end ? end : newCount
                })
            }, 15)

            return () => clearTimeout(timer)
        }
    }, [count, end, duration])

    return (
        <span>{prefix}{count}{suffix}</span>
    )
}

interface AnimatedElementProps {
    children: React.ReactNode;
    delay?: number;
    animation?: 'fadeIn' | 'fadeUp' | 'fadeRight' | 'zoomIn';
    className?: string;
}

export function AnimatedElement({ children, delay = 0, animation = 'fadeIn', className = '' }: AnimatedElementProps) {
    const [isVisible, setIsVisible] = useState(false)

    useEffect(() => {
        const timer = setTimeout(() => {
            setIsVisible(true)
        }, delay)

        return () => clearTimeout(timer)
    }, [delay])

    const getAnimationClass = () => {
        switch (animation) {
            case 'fadeUp':
                return 'opacity-0 translate-y-4'
            case 'fadeRight':
                return 'opacity-0 -translate-x-4'
            case 'zoomIn':
                return 'opacity-0 scale-95'
            default:
                return 'opacity-0'
        }
    }
    return (
        <div
            className={`transition-all duration-700 ease-out ${isVisible ? 'opacity-100 translate-y-0 translate-x-0 scale-100' : getAnimationClass()} ${className}`}
        >
            {children}
        </div>
    )
}

export function ParallaxSection({ children, intensity = 0.2 }: { children: React.ReactNode; intensity?: number }) {
    const divRef = React.useRef<HTMLDivElement>(null)

    useEffect(() => {
        const handleScroll = () => {
            const newOffset = window.pageYOffset
            if (divRef.current) {
                divRef.current.style.setProperty('--transform-value', `translateY(${newOffset * intensity}px)`)
            }
        }

        window.addEventListener('scroll', handleScroll)
        // Initial setup
        handleScroll()

        return () => {
            window.removeEventListener('scroll', handleScroll)
        }
    }, [intensity])

    return (
        <div
            ref={divRef}
            className="parallax-section"
        >
            {children}
        </div>
    )
}

export function RevealOnScroll({ children }: { children: React.ReactNode }) {
    const [isVisible, setIsVisible] = useState(false)
    const ref = React.createRef<HTMLDivElement>()
    
    useEffect(() => {
        const observer = new IntersectionObserver(
            ([entry]) => {
                if (entry.isIntersecting) {
                    setIsVisible(true)
                    observer.unobserve(entry.target)
                }
            },
            {
                root: null,
                rootMargin: '0px',
                threshold: 0.1
            }
        )

        const currentRef = ref.current
        if (currentRef) {
            observer.observe(currentRef)
        }        return () => {
            if (currentRef) {
                observer.unobserve(currentRef)
            }
        }
    }, [ref])

    return (
        <div
            ref={ref}
            className={`transition-opacity duration-1000 ${isVisible ? 'opacity-100' : 'opacity-0'}`}
        >
            {children}
        </div>
    )
}
