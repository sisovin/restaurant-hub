'use client'

import Image from 'next/image'
import { FaInstagram } from 'react-icons/fa'
import Link from 'next/link'

const images = [
    '/images/menu-2.jpg',
    '/images/menu-3.jpg',
    '/images/menu-4.jpg',
    '/images/menu-5.jpg',
    '/images/menu-6.jpg',
    '/images/menu-7.jpg',
]

export default function Instagram() {
    return (
        <section className="relative mt-10 w-full overflow-hidden">
            {/* Centered Instagram Icon Button */}
            <Link
                href="#"
                className="absolute z-10 top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-24 h-24 rounded-full bg-white flex items-center justify-center shadow-md"
            >
                <FaInstagram className="text-3xl text-gray-600" />
            </Link>

            {/* Image Grid */}
            <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-0">
                {images.map((src, idx) => (
                    <div key={idx} className="group relative">
                        <Image
                            src={src}
                            alt={`Instagram ${idx + 1}`}
                            width={400}
                            height={400}
                            className="w-full h-full object-cover transition-opacity duration-500 group-hover:opacity-90"
                        />
                    </div>
                ))}
            </div>
        </section>
    )
}
