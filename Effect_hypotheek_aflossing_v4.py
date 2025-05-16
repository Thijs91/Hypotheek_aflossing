import math
import matplotlib.pyplot as plt

def calculate_monthly_payment(principal, annual_rate, years):
    """ Bereken de standaard maandelijkse annuïteit """
    monthly_rate = annual_rate / 100 / 12.0 
    n = years * 12
    payment = principal * monthly_rate * (1 + monthly_rate) ** n / ((1 + monthly_rate) ** n - 1)
    return payment

def simulate_amortisation_schedule(principal, monthly_rate, monthly_payment, structural_extra=0, start_month_extra=1, one_time_payments=None):
    """ Simuleer de aflossing van de hypotheek en genereer een schema """
    if one_time_payments is None:
        one_time_payments = {}
        
    month = 0
    cumulative_interest = 0.0
    remaining_principal = principal
    schedule = []
    
    while remaining_principal > 1e-6:
        month += 1
        interest = remaining_principal * monthly_rate
        extra_one_time = one_time_payments.get(month, 0)
        
        # Pas de structurele extra aflossing toe vanaf de opgegeven startmaand
        current_structural_extra = 0 if month < start_month_extra else structural_extra
        
        total_payment = monthly_payment + current_structural_extra + extra_one_time
        principal_payment = total_payment - interest
        
        if principal_payment > remaining_principal:
            principal_payment = remaining_principal
            total_payment = interest + remaining_principal
            
        cumulative_interest += interest
        remaining_principal -= principal_payment
        
        schedule.append({
            "Maand": month,
            "Betaling": total_payment,
            "Rente": interest,
            "Aflossing": principal_payment,
            "Cumulatieve Rente": cumulative_interest,
            "Restschuld": remaining_principal
        })
    
    return schedule

def main():
    print("Berekening van een annuïteitenhypotheek met structurele en incidentele extra aflossingen\n")
    
    # Input van de gebruiker
    principal = float(input("Voer het initiële leenbedrag in (bijv. 300000): "))
    annual_rate = float(input("Voer het jaarlijkse rentepercentage in (bijv. 4.0): "))
    years = float(input("Voer de looptijd in jaren in (bijv. 30): "))
    
    # Bereken de standaard annuïteit
    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
    monthly_rate = annual_rate / 100 / 12.0
    print(f"\nStandaard maandlast (annuïteit): {monthly_payment:.2f}")

    # Vraag het structurele extra bedrag per maand en de startmaand
    structural_extra = float(input("Voer het structureel extra bedrag per maand in (bijv. 100): "))
    start_month_extra = int(input("Vanaf welke maand start de structurele extra aflossing? (bijv. 1): "))
    
    # Vraag naar eenmalige extra aflossingen
    one_time_payments = {}
    num_one_time = int(input("Hoeveel eenmalige extra aflossingen wil je toevoegen? "))
    for i in range(num_one_time):
        maand = int(input(f"Voer de maand in waarin de {i+1}e extra aflossing plaatsvindt: "))
        bedrag = float(input("Voer het bedrag van deze extra aflossing in: "))
        one_time_payments[maand] = one_time_payments.get(maand, 0) + bedrag

    # Simuleer beide scenario's
    schedule_standard = simulate_amortisation_schedule(principal, monthly_rate, monthly_payment)
    schedule_extra = simulate_amortisation_schedule(principal, monthly_rate, monthly_payment,
                                                    structural_extra, start_month_extra, one_time_payments)
    
    # Bepaal de maximale looptijd van beide scenario's
    max_months = max(len(schedule_standard), len(schedule_extra))

    # Vul het kortere schema aan met extra maanden waar nodig
    while len(schedule_standard) < max_months:
        last_entry = schedule_standard[-1]
        schedule_standard.append({
            "Maand": last_entry["Maand"] + 1,
            "Betaling": 0,
            "Rente": 0,
            "Aflossing": 0,
            "Cumulatieve Rente": last_entry["Cumulatieve Rente"],
            "Restschuld": 0
        })

    while len(schedule_extra) < max_months:
        last_entry = schedule_extra[-1]
        schedule_extra.append({
            "Maand": last_entry["Maand"] + 1,
            "Betaling": 0,
            "Rente": 0,
            "Aflossing": 0,
            "Cumulatieve Rente": last_entry["Cumulatieve Rente"],
            "Restschuld": 0
        })

    print("\nAflossingstabel:")
    header = f"{'Maand':>5} | {'Betaling ZONDER':>15} | {'Rente ZONDER':>15} | {'Aflossing ZONDER':>15} | {'C. Rente ZONDER':>15} | {'Restschuld ZONDER':>15} | {'Betaling MET':>15} | {'Rente MET':>15} | {'Aflossing MET':>15} | {'C. Rente MET':>15} | {'Restschuld MET':>15}"
    print(header)
    print("-" * len(header))

    for rec_std, rec_ext in zip(schedule_standard, schedule_extra):
        print(f"{rec_std['Maand']:5d} | {rec_std['Betaling']:15.2f} | {rec_std['Rente']:15.2f} | {rec_std['Aflossing']:15.2f} | {rec_std['Cumulatieve Rente']:15.2f} | {rec_std['Restschuld']:15.2f} "
              f"| {rec_ext['Betaling']:15.2f} | {rec_ext['Rente']:15.2f} | {rec_ext['Aflossing']:15.2f} | {rec_ext['Cumulatieve Rente']:15.2f} | {rec_ext['Restschuld']:15.2f}")

   
    # Definieer data voor grafiek
    months_standard = [rec["Maand"] for rec in schedule_standard]
    months_extra = [rec["Maand"] for rec in schedule_extra]
    remaining_debt_standard = [rec["Restschuld"] for rec in schedule_standard]
    remaining_debt_extra = [rec["Restschuld"] for rec in schedule_extra]
    cumulative_interest_standard = [rec["Cumulatieve Rente"] for rec in schedule_standard]
    cumulative_interest_extra = [rec["Cumulatieve Rente"] for rec in schedule_extra]

    # Zorg dat beide lijsten even lang zijn
    max_length = max(len(months_standard), len(months_extra), len(remaining_debt_standard), len(remaining_debt_extra))
    
    while len(months_standard) < max_length:
        months_standard.append(months_standard[-1])

    while len(months_extra) < max_length:
        months_extra.append(months_extra[-1])

    while len(remaining_debt_standard) < max_length:
        remaining_debt_standard.append(remaining_debt_standard[-1])

    while len(remaining_debt_extra) < max_length:
        remaining_debt_extra.append(remaining_debt_extra[-1])

    while len(cumulative_interest_standard) < max_length:
        cumulative_interest_standard.append(cumulative_interest_standard[-1])

    while len(cumulative_interest_extra) < max_length:
        cumulative_interest_extra.append(cumulative_interest_extra[-1])
    
    # Bereken de totale betaalde bedragen
    total_paid_standard = sum(rec["Betaling"] for rec in schedule_standard) # Alle maandelijkse betalingen zonder extra aflossingen
    total_paid_extra = sum(rec["Betaling"] for rec in schedule_extra)       # Alle maandelijkse betalingen inclusief extra aflossingen
    
    # Cumulatieve rente over beide scenario's
    cumulative_interest_standard_final = schedule_standard[-1]["Cumulatieve Rente"]
    cumulative_interest_extra_final = schedule_extra[-1]["Cumulatieve Rente"]
    cumulative_interest_diff = cumulative_interest_standard_final - cumulative_interest_extra_final

    # Bereken het aantal maanden dat je eerder klaar bent met aflossen
    months_standard_real = next((rec["Maand"] for rec in schedule_standard if rec["Restschuld"] <= 0), len(schedule_standard))
    months_extra_real = next((rec["Maand"] for rec in schedule_extra if rec["Restschuld"] <= 0), len(schedule_extra))
    months_saved = months_standard_real - months_extra_real

    # Totaal betaalde structurele extra aflossingen
    total_structural_extra = structural_extra * max(0, months_extra_real - (start_month_extra - 1))
    total_structural_extra_details = f"€ {structural_extra:.2f} per maand vanaf maand {start_month_extra} gedurende {max(0, months_extra_real - (start_month_extra - 1))} maanden"

    # Totaal betaalde incidentele extra aflossingen met details per maand
    total_incidental_extra = sum(one_time_payments.values())
    incidental_extra_details = ", ".join(f"€ {bedrag:.2f} in maand {maand}" for maand, bedrag in one_time_payments.items())

    # Bereken de totale extra aflossing
    total_extra = sum(
        (rec_extra["Aflossing"] - rec_standard["Aflossing"])
        for rec_extra, rec_standard in zip(schedule_extra, schedule_standard)
        if rec_extra["Aflossing"] > rec_standard["Aflossing"])

    # Bereken het sneeuwbaleffect
    total_snowball = total_extra - (total_structural_extra + total_incidental_extra)

    print("\n--- Eindoverzicht ---")
    print("--- Besparing in looptijd ---")
    print(f"Looptijd hypotheek zonder extra aflossingen: {months_standard_real} maanden ({months_standard_real/12:.1f} jaar)")
    print(f"Looptijd hypotheek met extra aflossingen: {months_extra_real} maanden ({months_extra_real/12:.1f} jaar)")
    print(f"Aantal maanden eerder klaar met aflossen: {months_saved} maanden ({months_saved/12:.1f} jaar)")
    
    print("\n--- Financiële besparing")
    print(f"Totaal betaald zonder extra aflossing (rente + aflossing): € {total_paid_standard:.2f}")
    print(f"Totaal betaald met extra aflossing(en) (rente + aflossing): € {total_paid_extra:.2f}")
    
    print(f"\nTotaal betaalde rente zonder extra aflossing(en): € {cumulative_interest_standard_final:.2f}")
    print(f"Totaal betaalde rente met extra aflossing(en): € {cumulative_interest_extra_final:.2f}")
    print(f"Totale besparing aan rente door extra af te lossen: € {cumulative_interest_diff:.2f}")
    
    print(f"\nTotaal aan structurele aflossing: € {total_structural_extra:.2f} ({total_structural_extra_details})")
    print(f"Totaal aan incidentele aflossingen: € {total_incidental_extra:.2f} ({incidental_extra_details})")
    print(f"Totaal aan sneeuwbaleffect aflossingen: € {total_snowball:.2f} ")
    print(f"Totaal extra aflossing (inclusief sneeuwbaleffect): € {total_extra:.2f}")

    # Maak de grafiek
    plt.figure(figsize=(10, 6))
    plt.plot(months_standard, remaining_debt_standard, label="Restschuld zonder extra aflossingen", color='blue', linestyle='--')
    plt.plot(months_extra, remaining_debt_extra, label="Restschuld met extra aflossingen", color='green')
    plt.plot(months_standard, cumulative_interest_standard, label="Cumulatieve Rente zonder extra aflossingen", color='red', linestyle='--')
    plt.plot(months_extra, cumulative_interest_extra, label="Cumulatieve Rente met extra aflossingen", color='orange')

    plt.title("Hypotheekaflossing over de tijd")
    plt.xlabel("Maand")
    plt.ylabel("Bedrag")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()