import matplotlib.pyplot as plt

# Increase default font size
plt.rcParams.update({'font.size': 16})

# Data
queries = ['TPCH 1', 'TPCH 6', 'I/O Dominate Select']
latency_method1 = [1.50, 0.635, 0.615]  # SQPOLL + HugePage + Registered File
latency_method2 = [1.36, 0.49, 0.45]    # ThreadPoll + pread
improvements = [-9.0, -23.0, -27.3]     # % improvements

# Plot
fig, ax = plt.subplots(figsize=(10, 3))

# Positions for bars
y_positions = range(len(queries))
bar_height = 0.4

# Horizontal bars
bars1 = ax.barh([y + bar_height/2 for y in y_positions], latency_method1, height=bar_height, label='ChainIO')
bars2 = ax.barh([y - bar_height/2 for y in y_positions], latency_method2, height=bar_height, label='Baseline')

# Annotate improvement percentages on the second method bars
for i, imp in enumerate(improvements):
    ax.text(latency_method2[i] + 0.02, y_positions[i] - bar_height/2, f'{imp:.1f}%', va='center')

# Styling without title, larger fonts
ax.set_yticks(y_positions)
ax.set_yticklabels(queries, fontsize=18)
ax.set_xlabel('Latency (s)', fontsize=18)
ax.tick_params(axis='x', labelsize=18)
ax.legend(fontsize=18)

plt.tight_layout()
plt.savefig('chainio.pdf')