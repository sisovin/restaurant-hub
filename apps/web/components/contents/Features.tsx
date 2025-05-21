'use client';

import { useEffect, useState } from 'react';
import Image from 'next/image';
import { Button } from '@/components/ui/button';

const features = [
    {
        title: 'Best Chef',
        image: '/images/feature-1.png',
        description:
            'Sed amet tempor amet sit kasd sea lorem dolor ipsum elitr dolor amet kasd elitr duo vero amet amet stet',
    },
    {
        title: 'Menu Variations',
        image: '/images/feature-2.png',
        description:
            'Sed amet tempor amet sit kasd sea lorem dolor ipsum elitr dolor amet kasd elitr duo vero amet amet stet',
    },
    {
        title: 'Healthy Food',
        image: '/images/feature-3.png',
        description:
            'Sed amet tempor amet sit kasd sea lorem dolor ipsum elitr dolor amet kasd elitr duo vero amet amet stet',
    },
];

export default function Features() {
    const [mounted, setMounted] = useState(false);

    useEffect(() => {
        setMounted(true);
    }, []);

    return (
        <section className="relative mb-[135px]">
            {/* Simulate ::after background */}
            <div className="absolute top-[135px] left-0 w-full h-[calc(100%-45px)] bg-[#1d1f23] -z-10" />

            <div className="container mx-auto px-4 pt-20">
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
                    {features.map((feature, index) => (
                        <div
                            key={index}
                            className={`rounded-lg text-center shadow-md transition-opacity duration-1000 overflow-hidden bg-gradient-to-b from-gray-100 via-gray-100 to-[#1d1f23] ${mounted ? 'opacity-100' : 'opacity-0'
                                }`}
                        >
                            <div className="flex justify-center mt-8">
                                <div className="w-[150px] h-[150px] bg-white rounded-full flex items-center justify-center shadow-md">
                                    <Image
                                        src={feature.image}
                                        alt={feature.title}
                                        width={100}
                                        height={100}
                                        className="object-contain"
                                    />
                                </div>
                            </div>
                            <div className="p-6 pt-4">
                                <h3 className="text-2xl font-bold mb-4 font-body text-gray-800">{feature.title}</h3>
                                <p className="text-sm text-gray-600 mb-4">{feature.description}</p>
                                <a
                                    href="#"
                                    className="text-orange-500 hover:text-orange-600 font-semibold tracking-wide inline-flex items-center transition-colors"
                                >
                                    Read More <span className="ml-1">→</span>
                                </a>
                            </div>
                        </div>
                    ))}
                </div>

                <div
                    className={`text-center transition-opacity duration-1000 ${mounted ? 'opacity-100' : 'opacity-0'
                        }`}
                >
                    <h2 className="text-4xl md:text-5xl lg:text-6xl font-bold font-display mb-6">
                        <span className="text-orange-500 block">30% Discount</span>
                        <span className="text-gray-300 block italic">For This Summer</span>
                    </h2>
                    <Button
                        className="bg-orange-500 hover:bg-orange-600 text-white text-lg px-8 py-4 rounded-md font-semibold shadow-md"
                        asChild
                    >
                        <a href="#">Order Now</a>
                    </Button>
                </div>
            </div>
        </section>
    );
}
