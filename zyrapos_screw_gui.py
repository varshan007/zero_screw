import streamlit as st

def get_biomass_properties(biomass_type):
    biomass_database = {
        "Paddy Straw": {"bulk_density": 120, "particle_size": 20},
        "Wheat Straw": {"bulk_density": 110, "particle_size": 15},
        "Sugarcane Bagasse": {"bulk_density": 150, "particle_size": 10},
        "Corn Stover": {"bulk_density": 130, "particle_size": 12},
        "Cotton Stalks": {"bulk_density": 100, "particle_size": 18},
        "Sawdust": {"bulk_density": 220, "particle_size": 2},
        "Wood Chips": {"bulk_density": 180, "particle_size": 25}
    }
    return biomass_database.get(biomass_type)

st.title("ZyraPod Screw Conveyor Designer")

biomass_type = st.selectbox("Select Biomass Type", list(get_biomass_properties("").keys()))
feed_rate = st.number_input("Feed Rate (kg/hr)", min_value=1, max_value=500, value=50)

if biomass_type:
    props = get_biomass_properties(biomass_type)
    bd = props["bulk_density"]
    ps = props["particle_size"]

    feed_rate_m3_min = (feed_rate / 60) / bd

    if ps <= 10:
        screw_dia = 75
    elif ps <= 20:
        screw_dia = 100
    else:
        screw_dia = 125

    pitch = screw_dia
    shaft_dia = int(screw_dia * 0.25)
    rpm = 45 if screw_dia <= 100 else 35
    motor_power_kW = 0.18 if feed_rate <= 25 else 0.37

    st.subheader("Recommended Conveyor Specs:")
    st.write(f"**Screw Diameter:** {screw_dia} mm")
    st.write(f"**Pitch:** {pitch} mm")
    st.write(f"**Shaft Diameter:** {shaft_dia} mm")
    st.write(f"**Length:** 1–1.5 m")
    st.write(f"**RPM:** {rpm}")
    st.write(f"**Housing:** U-trough or pipe")
    st.write(f"**Motor Power:** {motor_power_kW:.2f} kW")
    st.write(f"**Gearbox:** Worm or helical type")
