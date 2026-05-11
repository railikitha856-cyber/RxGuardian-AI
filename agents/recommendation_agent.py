def adherence_advice(medicine):

    med = medicine.lower()

    if med == "ibuprofen":
        return [
            "Take after food",
            "Avoid alcohol",
            "Do not exceed recommended dosage"
        ]

    if med == "amoxicillin":
        return [
            "Complete full antibiotic course",
            "Take at same time daily",
            "Do not skip doses"
        ]

    return [
        "Follow prescription instructions carefully"
    ]