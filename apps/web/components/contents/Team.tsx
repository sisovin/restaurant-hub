'use client'

import Image from 'next/image'
import Link from 'next/link'
import { FaFacebookF, FaTwitter, FaLinkedinIn } from 'react-icons/fa'

const teamMembers = [
    {
        name: 'John Deo',
        role: 'Master Chef',
        image: '/images/team-1.jpg',
    },
    {
        name: 'John Deo',
        role: 'Assistant',
        image: '/images/team-2.jpg',
    },
    {
        name: 'John Deo',
        role: 'Assistant',
        image: '/images/team-3.jpg',
    },
]

export default function Team() {
    return (
        <section className="w-full px-5 py-20 bg-white">
            <div className="mb-12 text-center mx-auto">
                <h5 className="text-orange-500 text-lg font-semibold uppercase tracking-wide mb-2">
                    Expert Chefs
                </h5>
                <h1 className="text-4xl md:text-5xl font-bold text-gray-800">
                    Let&apos;s Meet The Expert
                </h1>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-10 w-full">
                {teamMembers.map((member, index) => (
                    <div
                        key={index}
                        className="relative group overflow-hidden rounded-tl-[40%] transition-all duration-500 w-full"
                    >
                        {/* Image wrapper */}
                        <div className="relative aspect-[3/4] w-full overflow-hidden">
                            <Image
                                src={member.image}
                                alt={member.name}
                                fill
                                className="object-cover transition-transform duration-500 group-hover:scale-110"
                            />

                            {/* Social Overlay */}
                            <div className="absolute inset-0 bg-black/80 opacity-0 group-hover:opacity-100 flex items-center justify-center transition-opacity duration-500 z-10">
                                <div className="flex space-x-3">
                                    {[FaTwitter, FaFacebookF, FaLinkedinIn].map((Icon, i) => (
                                        <Link
                                            href="#"
                                            key={i}
                                            className="bg-white text-black p-2 rounded-full hover:bg-gray-200 transition"
                                        >
                                            <Icon className="w-4 h-4" />
                                        </Link>
                                    ))}
                                </div>
                            </div>
                        </div>

                        {/* Name & Role */}
                        <div className="absolute bottom-0 left-0 w-full h-[90px] flex flex-col justify-center items-center text-center bg-black/90 text-white z-20">
                            <h5 className="text-white text-base font-semibold">{member.name}</h5>
                            <p className="text-xs uppercase text-gray-400 tracking-widest">{member.role}</p>
                        </div>
                    </div>
                ))}
            </div>
        </section>
    )
}
