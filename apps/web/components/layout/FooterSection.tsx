'use client'
import React from 'react'
import Link from 'next/link'
import { AnimatedElement } from '../animation'

export default function FooterSection() {
    return (
        <>
            {/* Footer Start */}
            <div className="bg-zinc-900 text-neutral-400 pt-10">
                <div className="container mx-auto px-6 md:px-10 lg:px-16">
                    <div className="flex flex-col lg:flex-row gap-12 lg:gap-20">
                        {/* Left Column - Contact Info */}                        <AnimatedElement animation="fadeIn" delay={100} className="flex-1 space-y-4">
                            <h4 className="text-white text-2xl font-body mb-4">Get In Touch</h4>
                            <div className="flex items-start gap-2">
                                <i className="bi bi-geo-alt text-orange-500 mt-1"></i>
                                <p className="font-body">123 Street, New York, USA</p>
                            </div>
                            <div className="flex items-start gap-2">
                                <i className="bi bi-envelope-open text-orange-500 mt-1"></i>
                                <p className="font-body">info@example.com</p>
                            </div>
                            <div className="flex items-start gap-2">
                                <i className="bi bi-telephone text-orange-500 mt-1"></i>
                                <p>+012 345 6789</p>
                            </div>

                            <div className="flex gap-3 pt-4">
                                {['twitter', 'facebook-f', 'linkedin-in', 'instagram'].map((icon) => (
                                    <Link
                                        key={icon}
                                        href="#"
                                        className="w-10 h-10 flex items-center justify-center border border-orange-500 text-white rounded-full bg-orange-500 hover:text-gray-300 transition"
                                        aria-label={icon}
                                    >
                                        <i className={`fab fa-${icon}`}></i>
                                    </Link>
                                ))}
                            </div>
                        </AnimatedElement>                        {/* Middle Column - Quick Links */}
                        <AnimatedElement animation="fadeIn" delay={300} className="flex-1 space-y-4">
                            <h4 className="text-white text-2xl font-body mb-4">Quick Links</h4>
                            {[
                                ['/', 'Home'],
                                ['/about', 'About Us'],
                                ['/menu', 'Food Menu'],
                                ['/team', 'Our Chefs'],
                                ['/blog', 'Latest Blog'],
                                ['/contact', 'Contact Us'],
                            ].map(([href, label]) => (
                                <Link key={label} href={href} className="flex items-center text-neutral-400 hover:text-white mb-1 font-body">
                                    <i className="bi bi-arrow-right text-orange-500 mr-2"></i> {label}
                                </Link>
                            ))}
                        </AnimatedElement>                        {/* Right Column - More Links */}
                        <AnimatedElement animation="fadeIn" delay={500} className="flex-1 space-y-4">
                            <h4 className="text-white text-2xl font-body mb-4">More Links</h4>
                            {[
                                ['/about', 'About Us'],
                                ['/menu', 'Food Menu'],
                                ['/team', 'Our Chefs'],
                                ['/blog', 'Latest Blog'],
                                ['/contact', 'Contact Us'],
                            ].map(([href, label]) => (
                                <Link key={label} href={href} className="flex items-center text-neutral-400 hover:text-white mb-1 font-body">
                                    <i className="bi bi-arrow-right text-orange-500 mr-2"></i> {label}
                                </Link>
                            ))}
                        </AnimatedElement>                        {/* Newsletter */}
                        <AnimatedElement animation="fadeIn" delay={700} className="col-lg-4 col-md-6">
                            <div className="flex flex-col items-start justify-center h-full p-6 bg-[#f75006] text-white rounded-md">
                                <h4 className="text-white text-2xl font-body mb-2">Newsletter</h4>
                                <h5 className="text-white text-lg font-body uppercase mb-1">Subscribe Our Newsletter</h5>
                                <p className="text-white text-sm mb-4 leading-snug font-body">
                                    Amet justo diam dolor rebum lorem sit stet sea justo kasd
                                </p>                                <form className="w-full">
                                    <div className="flex w-full">
                                        <input
                                            type="email"
                                            placeholder="Your Email"
                                            className="flex-grow p-3 text-black placeholder-black bg-white border-none focus:outline-none font-body"
                                        />
                                        <button
                                            type="submit"
                                            className="bg-black text-white hover:text-gray-300 px-4 py-3 font-body font-bold"
                                        >
                                            Sign Up
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </AnimatedElement>

                    </div>
                </div>                {/* Bottom Footer */}
                <div className="border-t border-neutral-700 mt-10 py-4 px-6 bg-black">
                    <div className="container mx-auto flex flex-col md:flex-row justify-between items-center text-sm text-white">
                        <p className="font-body">
                            &copy; <Link href="/" className="underline font-body">Your Site Name</Link>. All Rights Reserved.
                        </p>
                        <p className="font-body">
                            Designed by <Link href="https://htmlcodex.com" className="underline font-body">HTML Codex</Link>
                        </p>
                    </div>
                </div>
            </div>
            {/* Footer End */}
        </>
    )
}
