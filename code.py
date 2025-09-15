# Minimal interactive GD widget (PyTorch)
# pip install torch ipywidgets pandas matplotlib
import os, pandas as pd, torch, matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# --- Load data ---
fp = "/Users/murff/Library/CloudStorage/OneDrive-BrighamYoungUniversity/3. Teaching/strategy-prototyping/data/home-price-data.csv"
if os.path.exists(fp):
    df = pd.read_csv(fp)
    x_raw = torch.tensor(df["size"].values, dtype=torch.float32).view(-1,1)
    y = torch.tensor(df["price"].values, dtype=torch.float32).view(-1,1)
else:
    # fallback demo data if path isn't available in your environment
    torch.manual_seed(0)
    x_raw = torch.linspace(400.0, 2400.0, 60).view(-1,1)
    y = 12.0*x_raw + 50.0 + torch.randn_like(x_raw)*120.0

# --- Standardize x for stable training; display in original units ---
x_mean, x_std = x_raw.mean(), x_raw.std()
x = (x_raw - x_mean) / (x_std + 1e-8)

model = torch.nn.Linear(1,1)
opt   = torch.optim.SGD(model.parameters(), lr=0.05)
lossf = torch.nn.MSELoss()

# plotting setup
fig, ax = plt.subplots(figsize=(6,4))
ax.scatter(x_raw.numpy(), y.numpy(), s=15)
xg = torch.linspace(x.min(), x.max(), 200).view(-1,1)
xg_orig = xg*(x_std+1e-8)+x_mean
ln, = ax.plot(xg_orig.numpy(), model(xg).detach().numpy())
ax.set_xlabel("size"); ax.set_ylabel("price"); ax.set_title("Click Next to train")
plt.tight_layout()
plt.show()

losses = []
loss_lbl = widgets.Label()

def update_plot_and_label():
    with torch.no_grad():
        yg = model(xg)
        ln.set_ydata(yg.numpy())
    loss = lossf(model(x), y).item()
    losses.append(loss)
    W = model.weight.item()/(x_std.item()+1e-8)
    B = model.bias.item() - model.weight.item()*x_mean.item()/(x_std.item()+1e-8)
    loss_lbl.value = f"Loss: {loss:.4f}   |   W≈{W:.4f}, B≈{B:.4f}"
    fig.canvas.draw_idle()

def on_next(_):
    opt.zero_grad()
    loss = lossf(model(x), y)
    loss.backward()
    opt.step()
    update_plot_and_label()

def on_reset(_):
    global model, opt, losses
    model = torch.nn.Linear(1,1)
    opt   = torch.optim.SGD(model.parameters(), lr=0.05)
    losses = []
    update_plot_and_label()

next_btn  = widgets.Button(description="Next")
reset_btn = widgets.Button(description="Reset")
next_btn.on_click(on_next)
reset_btn.on_click(on_reset)

update_plot_and_label()
display(widgets.HBox([next_btn, reset_btn]))
display(loss_lbl)

# Optional: show loss curve updating live (simple)
import matplotlib.pyplot as plt
fig2, ax2 = plt.subplots(figsize=(6,3.5))
(line_loss,) = ax2.plot(range(len(losses)), losses)
ax2.set_xlabel("iteration"); ax2.set_ylabel("MSE"); ax2.set_title("Training loss")
plt.tight_layout()
plt.show()

def on_next_with_curve(_):
    on_next(_)
    line_loss.set_xdata(range(len(losses)))
    line_loss.set_ydata(losses)
    ax2.relim(); ax2.autoscale_view(); fig2.canvas.draw_idle()

next_btn.on_click(on_next_with_curve)  # rebind to also refresh the loss curve
