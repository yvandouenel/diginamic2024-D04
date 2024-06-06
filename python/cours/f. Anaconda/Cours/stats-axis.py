import pandas as pd

data = {
    'Formation': ['Mathématiques', 'Physique', 'Français', 'Anglais', 'autre'],
    'Étudiant': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Note': [85, 92, 78, 95, 88]
}

df_notes = pd.DataFrame(data)
df_notes.set_index(['Formation', 'Étudiant'], inplace=True)

print("*"*50)
print(df_notes)

print("*"*50)
print(df_notes.sum(axis=1))

print("*"*50)
print(df_notes.mean(axis=1))

print("*"*50)
print(df_notes.max())

print("*"*50)
print(df_notes['Mathématiques'].describe())