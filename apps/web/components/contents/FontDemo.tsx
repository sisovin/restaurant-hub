'use client';

export default function FontDemo() {
    return (
        <div className="container mx-auto py-8 px-4">
            <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
                <h2 className="font-heading text-3xl mb-6">Font Typography Preview</h2>

                <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                    {/* Emblema One Section */}
                    <div className="border rounded-md p-4">
                        <h3 className="font-heading text-2xl mb-4">Emblema One Font</h3>
                        <div className="space-y-4">
                            <div>
                                <h1 className="font-heading text-4xl">Heading 1 (h1)</h1>
                                <p className="text-gray-500 text-sm mt-1">Font-family: Emblema One, Font-weight: 400</p>
                            </div>
                            <div>
                                <h2 className="font-heading text-3xl">Heading 2 (h2)</h2>
                                <p className="text-gray-500 text-sm mt-1">Font-family: Emblema One, Font-weight: 400</p>
                            </div>
                            <div>
                                <h3 className="font-heading text-2xl">Heading 3 (h3)</h3>
                                <p className="text-gray-500 text-sm mt-1">Font-family: Emblema One, Font-weight: 400</p>
                            </div>
                            <div>
                                <p className="font-heading text-xl">.font-heading Class</p>
                                <p className="text-gray-500 text-sm mt-1">Font-family: Emblema One, Font-weight: 400</p>
                            </div>
                        </div>
                    </div>

                    {/* Poppins Section */}
                    <div className="border rounded-md p-4">
                        <h3 className="font-heading text-2xl mb-4">Poppins Font</h3>
                        <div className="space-y-4">
                            <div>
                                <h4 className="text-xl">Heading 4 (h4)</h4>
                                <p className="text-gray-500 text-sm mt-1">Font-family: Poppins, Font-weight: 600</p>
                            </div>
                            <div>
                                <h5 className="text-lg">Heading 5 (h5)</h5>
                                <p className="text-gray-500 text-sm mt-1">Font-family: Poppins, Font-weight: 500</p>
                            </div>
                            <div>
                                <h6 className="text-base">Heading 6 (h6)</h6>
                                <p className="text-gray-500 text-sm mt-1">Font-family: Poppins, Font-weight: 400</p>
                            </div>
                            <div>
                                <p className="font-body text-base">.font-body Class</p>
                                <p className="text-gray-500 text-sm mt-1">Font-family: Poppins, Font-weight: 400</p>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Display Classes */}
                <div className="border rounded-md p-4 mb-6">
                    <h3 className="font-heading text-2xl mb-4">Display Classes</h3>
                    <div className="space-y-4">
                        <div>
                            <p className="display-1">Display 1</p>
                            <p className="text-gray-500 text-sm mt-1">Font-family: Emblema One</p>
                        </div>
                        <div>
                            <p className="display-4">Display 4</p>
                            <p className="text-gray-500 text-sm mt-1">Font-family: Poppins</p>
                        </div>
                    </div>
                </div>

                <p className="text-sm text-gray-600 italic">
                    This component demonstrates how the custom fonts are applied to different elements.
                    You can refer to this when designing your site to ensure consistency.
                </p>
            </div>
        </div>
    );
}
