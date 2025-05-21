'use client';

import { Star, Users, Check, Coffee } from 'lucide-react';
import { useEffect, useState, useRef } from 'react';
import styles from './Facts.module.css';

const facts = [
    {
        icon: <Star className="text-orange-500 w-6 h-6" />,
        label: 'Years',
        value: 1234,
    },
    {
        icon: <Users className="text-orange-500 w-6 h-6" />,
        label: 'Clients',
        value: 1234,
    },
    {
        icon: <Check className="text-orange-500 w-6 h-6" />,
        label: 'Awards',
        value: 1234,
    },
    {
        icon: <Coffee className="text-orange-500 w-6 h-6" />,
        label: 'Events',
        value: 1234,
    },
];

export default function Facts() {
    const [counters, setCounters] = useState<{ [key: number]: number }>({});
    const sectionRef = useRef<HTMLElement>(null);
    const animatedRef = useRef<boolean>(false);

    useEffect(() => {
        const startCounters = () => {
            if (animatedRef.current) return;

            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        animatedRef.current = true;

                        facts.forEach((fact, idx) => {
                            const target = fact.value;
                            let current = 0;
                            const duration = 2000; // 2 seconds
                            const increment = Math.ceil(target / (duration / 15)); // Update every 15ms
                            const startTime = Date.now();

                            const updateCounter = () => {
                                const elapsedTime = Date.now() - startTime;

                                if (elapsedTime < duration) {
                                    current += increment;
                                    if (current > target) current = target;

                                    setCounters(prev => ({ ...prev, [idx]: current }));
                                    requestAnimationFrame(updateCounter);
                                } else {
                                    setCounters(prev => ({ ...prev, [idx]: target }));
                                }
                            };

                            setTimeout(() => {
                                updateCounter();
                            }, idx * 100); // Stagger the animations
                        });

                        observer.disconnect();
                    }
                });
            }, { threshold: 0.1 });

            if (sectionRef.current) {
                observer.observe(sectionRef.current);
            }
        };

        startCounters();

        return () => {
            // Cleanup
        };
    }, []);

    return (
        <section ref={sectionRef} className="bg-[#1d1f23] py-16">
            <div className="container mx-auto px-4 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
                {facts.map((fact, index) => (
                    <div
                        key={index}
                        className={`flex items-center gap-4 ${styles.fadeIn} ${styles[`delay-${index}`]}`}
                        
                    >
                        <div className="rounded-full bg-[#111111] w-20 h-20 flex items-center justify-center shadow-md">
                            {fact.icon}
                        </div>
                        <div>
                            <h5 className="text-white font-semibold">{fact.label}</h5>                            <h1 className="text-4xl font-bold text-[#757575]" data-toggle="counter-up">
                                {counters[index] !== undefined ? counters[index] : 0}
                            </h1>
                        </div>
                    </div>
                ))}
            </div>
        </section>
    );
}
