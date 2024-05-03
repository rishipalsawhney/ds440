# import matplotlib
# matplotlib.use('TkAgg')  # or any other backend that works for you
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Read data from CSV file
# df = pd.read_csv('States.csv')  # Replace 'your_file.csv' with the actual path to your CSV file
#
# # Convert date strings to datetime objects
# df['date'] = pd.to_datetime(df['date'])
#
# # Aggregate data by date and state
# df_grouped = df.groupby(['date', 'state']).sum().reset_index()
#
# # Pivot data for stream graph
# pivot_df = df_grouped.pivot(index='date', columns='state', values='cases').fillna(0)
#
# # Plotting stream graph
# fig, ax = plt.subplots(figsize=(10, 6))
# pivot_df.plot(kind='area', stacked=True, ax=ax)
#
# # Beautify the plot
# plt.title('Confirmed Cases Over Time by State')
# plt.xlabel('Date')
# plt.ylabel('Confirmed Cases')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg' depending on your preference
import pandas as pd
# import matplotlib.pyplot as plt
#
# # Read data from CSV file
# df = pd.read_csv('States.csv')  # Replace 'your_file.csv' with the actual path to your CSV file
#
# # Convert date strings to datetime objects
# df['date'] = pd.to_datetime(df['date'])
#
# # Set 'date' column as the index
# df.set_index('date', inplace=True)
#
# # Resample data by week and state, summing the cases
# df_weekly = df.resample('W').sum()
#
# # Plotting stream graph
# fig, ax = plt.subplots(figsize=(14, 8))
# df_weekly.plot(kind='area', stacked=True, ax=ax, colormap='tab20')
#
# # Beautify the plot
# plt.title('Confirmed Cases Over Time by State (Aggregated by Week)')
# plt.xlabel('Date')
# plt.ylabel('Confirmed Cases')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.legend(loc='upper left', bbox_to_anchor=(1, 1), title='State')
# plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt
# from ipywidgets import interact, widgets
# from IPython.display import display
#
# # Read data from CSV file
# df = pd.read_csv('States.csv')  # Replace 'States.csv' with the actual path to your CSV file
#
# # Convert date strings to datetime objects
# df['date'] = pd.to_datetime(df['date'])
#
# # Aggregate data by date and state
# df_grouped = df.groupby(['date', 'state']).sum().reset_index()
#
# # Pivot data for stream graph
# pivot_df = df_grouped.pivot(index='date', columns='state', values='cases').fillna(0)
#
# def plot_progression(state):
#     plt.figure(figsize=(10, 6))
#     plt.fill_between(pivot_df.index, pivot_df[state], color='skyblue', alpha=0.4)
#     plt.plot(pivot_df.index, pivot_df[state], color='Slateblue', alpha=0.6, linewidth=2)
#     plt.title(f'Progression of Confirmed Cases for {state}')
#     plt.xlabel('Date')
#     plt.ylabel('Confirmed Cases')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()
#
# # Create dropdown menu
# state_dropdown = widgets.Dropdown(
#     options=df['state'].unique(),
#     description='Select State:',
#     disabled=False,
# )
#
# # Display dropdown and progression graph
# display(state_dropdown)
# interact(plot_progression, state=state_dropdown)
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Read data from CSV file
# df = pd.read_csv('States.csv')  # Replace 'States.csv' with the actual path to your CSV file
#
# # Convert date strings to datetime objects
# df['date'] = pd.to_datetime(df['date'])
#
# # Aggregate data by date and state
# df_grouped = df.groupby(['date', 'state']).sum().reset_index()
#
# # Pivot data for stream graph
# pivot_df = df_grouped.pivot(index='date', columns='state', values='cases').fillna(0)
#
# # Manually change the state to visualize its progression
# states = pivot_df.columns
#
# for state in states:
#     plt.figure(figsize=(10, 6))
#     plt.fill_between(pivot_df.index, pivot_df[state], color='skyblue', alpha=0.4)
#     plt.plot(pivot_df.index, pivot_df[state], color='Slateblue', alpha=0.6, linewidth=2)
#     plt.title(f'Progression of Confirmed Cases for {state}')
#     plt.xlabel('Date')
#     plt.ylabel('Confirmed Cases')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()
#     input("Press Enter to see the next state or Ctrl+C to exit:")
# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Read data from CSV file
# df = pd.read_csv('States.csv')  # Replace 'States.csv' with the actual path to your CSV file
#
# # Convert date strings to datetime objects
# df['date'] = pd.to_datetime(df['date'])
#
# # Aggregate data by date and state
# df_grouped = df.groupby(['date', 'state']).sum().reset_index()
#
# # Pivot data for stream graph
# pivot_df = df_grouped.pivot(index='date', columns='state', values='cases').fillna(0)
#
# # Get the list of states
# states = pivot_df.columns
#
# # Display the list of states and prompt the user to choose
# print("Select a state:")
# for i, state in enumerate(states):
#     print(f"{i+1}: {state}")
#
# # Get user input for the state index
# state_index = int(input("Enter the index of the state you want to visualize: ")) - 1
#
# # Check if the input index is valid
# if 0 <= state_index < len(states):
#     # Plot the progression of confirmed cases for the selected state
#     state = states[state_index]
#     plt.figure(figsize=(10, 6))
#     plt.fill_between(pivot_df.index, pivot_df[state], color='skyblue', alpha=0.4)
#     plt.plot(pivot_df.index, pivot_df[state], color='Slateblue', alpha=0.6, linewidth=2)
#     plt.title(f'Progression of Confirmed Cases for {state}')
#     plt.xlabel('Date')
#     plt.ylabel('Confirmed Cases')
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.show()
# else:
#     print("Invalid state index. Please enter a valid index.")
import re

# Read the sentences from the text file
with open('translationtovietnamese.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Extracting Hindi sentences
hindi_sentences = re.findall(r'Translated Vietnamese: (.+)', text)

# Write Hindi sentences to another text file
with open('viet_sentences.txt', 'w', encoding='utf-8') as file:
    for sentence in hindi_sentences:
        file.write(sentence.strip() + '\n')

