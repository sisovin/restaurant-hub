'use client';

import { useState } from 'react';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import Image from 'next/image';

const menuData = {
    breakfast: [
        'menu-1.jpg', 'menu-2.jpg', 'menu-3.jpg', 'menu-4.jpg',
        'menu-5.jpg', 'menu-6.jpg', 'menu-7.jpg', 'menu-8.jpg'
    ],
    lunch: [
        'menu-2.jpg', 'menu-3.jpg', 'menu-4.jpg', 'menu-5.jpg',
        'menu-6.jpg', 'menu-7.jpg', 'menu-8.jpg', 'menu-1.jpg'
    ],
    dinner: [
        'menu-3.jpg', 'menu-4.jpg', 'menu-5.jpg', 'menu-6.jpg',
        'menu-7.jpg', 'menu-8.jpg', 'menu-1.jpg', 'menu-2.jpg'
    ]
};

export default function Menu() {
    const [tab, setTab] = useState('breakfast');

    return (
        <section className="w-full py-20 px-4 bg-[#1d1f23]">
            <div className="max-w-full mx-auto text-center">
                <h5 className="text-orange-500 uppercase tracking-wide font-semibold mb-2">
                    Our Menu
                </h5>
                <h1 className="text-4xl lg:text-5xl font-bold text-white mb-10">
                    Hands Craft More Than Meals
                </h1>                <Tabs value={tab} onValueChange={setTab} className="w-full">
                    <div className="flex justify-center mb-10">
                        <TabsList className="bg-black text-white rounded-full p-1 flex space-x-4 mx-auto">

                            <TabsTrigger
                                value="breakfast"
                                className="rounded-full px-6 py-2 data-[state=active]:bg-orange-500 data-[state=active]:text-white"
                            >
                                Breakfast
                            </TabsTrigger>
                            <TabsTrigger
                                value="lunch"
                                className="rounded-full px-6 py-2 transition-colors duration-200 data-[state=active]:bg-orange-500 data-[state=active]:text-white data-[state=active]:shadow-md"
                            >
                                Lunch
                            </TabsTrigger>
                            <TabsTrigger
                                value="dinner"
                                className="rounded-full px-6 py-2 data-[state=active]:bg-orange-500 data-[state=active]:text-white"
                            >
                                Dinner
                            </TabsTrigger>
                        </TabsList>
                    </div>

                    {Object.entries(menuData).map(([key, items]) => (
                        <TabsContent key={key} value={key} className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                            {items.map((img, i) => (
                                <div key={i} className="relative group overflow-hidden rounded-lg">
                                    <Image
                                        src={`/images/${img}`}
                                        alt="Menu item"
                                        width={300}
                                        height={300}
                                        className="w-full h-auto transition-transform duration-300 group-hover:scale-105"
                                    />
                                    <div className="absolute bottom-4 right-4 bg-black text-orange-400 text-sm font-medium py-1 px-3 rounded-full shadow-lg">
                                        BBQ Chicken
                                    </div>
                                </div>
                            ))}
                        </TabsContent>
                    ))}
                </Tabs>
            </div>
        </section>
    );
}

