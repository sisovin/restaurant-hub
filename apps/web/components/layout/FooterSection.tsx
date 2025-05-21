'use client'
import React from 'react'
import Link from 'next/link'
import { AnimatedElement } from '../animation'
import SocialGroups from './SocialGroups'
import { MapPin, Mail, Phone, ArrowRight } from 'lucide-react'

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
                                <MapPin size={18} className="text-orange-500 mt-1" />
                                <p className="font-body">123 Street, New York, USA</p>
                            </div>
                            <div className="flex items-start gap-2">
                                <Mail size={18} className="text-orange-500 mt-1" />
                                <p className="font-body">info@example.com</p>
                            </div>
                            <div className="flex items-start gap-2">
                                <Phone size={18} className="text-orange-500 mt-1" />
                                <p>+012 345 6789</p>
                            </div>
                            {/* Footer Social Groups */}
                            <div className="pt-4">
                                <SocialGroups />
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
                                    <ArrowRight size={16} className="text-orange-500 mr-2" /> {label}
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
                                    <ArrowRight size={16} className="text-orange-500 mr-2" /> {label}
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
                </div>
                {/* Bottom Footer */}
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
