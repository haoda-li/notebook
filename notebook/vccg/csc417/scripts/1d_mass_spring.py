import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class TimeIntegration:
    def __init__(self, mass, stiffness, dt, q0, v0):
        """
        mass: the mass of the object
        stiffness: the stiffness coefficient of the spring
        dt: Delta t for each step taken
        q0: the initial position at t0
        v0: the initial velocity at t0
        """
        self.m = mass
        self.k = stiffness
        self.dt = dt
        self.q0 = q0
        self.v0 = v0
        self.trajectory_q = [q0]
        self.trajectory_v = [v0]

    def one_step(self):
        raise NotImplementedError

    def run(self, step):
        for _ in range(step):
            self.one_step()

    def plot(self, step, output_file):
        self.run(step)
        fig = make_subplots(rows=1, cols=2,
                            subplot_titles=('Object', 'Phase Space'),
                            column_widths=[0.7, 0.3])

        fig.add_trace(go.Scatter(x=[0, self.q0], y=[
                      0, 0], marker_size=10), 1, 1)

        fig.add_trace(go.Scatter(x=[self.q0], y=[
                      self.v0], marker_size=3), 1, 2)
        fig.frames = [go.Frame(data=[go.Scatter(x=[0, self.trajectory_q[i]]),
                                     go.Scatter(x=self.trajectory_q[:i], y=self.trajectory_v[:i])],
                               traces=[0, 1]) for i in range(len(self.trajectory_q))]
        button = dict(
            label='Play',
            method='animate',
            args=[None, dict(
                frame=dict(duration=50, redraw=False),
                transition=dict(duration=0),
                fromcurrent=True,
                mode='immediate')])
        fig.update_layout(
            updatemenus=[
                dict(
                    type='buttons',
                    showactive=False,
                    y=0,
                    x=1.05,
                    xanchor='left',
                    yanchor='bottom',
                    buttons=[button])
            ],
            showlegend=False
        )
        fig.update_xaxes(range=[-3, 3])
        fig.update_yaxes(range=[-20, 20])
        fig.write_html(output_file, full_html=False, auto_open=False,
                       include_plotlyjs="cdn", auto_play=False)


mass = 1
stiffness = 100
dt = 0.01
q0 = 1
v0 = 1

STEPS=75

# --8<-- [start:fe]
class ForwardEuler(TimeIntegration):
    def one_step(self):
        q_t = self.trajectory_q[-1]
        v_t = self.trajectory_v[-1]
        self.trajectory_v.append(v_t - self.dt * self.k / self.m * q_t)
        self.trajectory_q.append(q_t + self.dt * v_t)
# --8<-- [end:fe]
fe = ForwardEuler(mass, stiffness, dt, q0, v0)
fe.plot(STEPS, "../assets/1d_mass_spring_fe.html")

# --8<-- [start:rk4]
class RK4(TimeIntegration):
    def one_step(self):
        q_t = self.trajectory_q[-1]
        v_t = self.trajectory_v[-1]
        weights = np.array((1, 2, 2, 1))
        kappa = np.empty((4, 2))
        kappa[0, 0] = v_t
        kappa[0, 1] = - self.k / self.m * q_t
        
        kappa[1, 0] = v_t + self.dt * 0.5 * kappa[0, 1]
        kappa[1, 1] = - self.k / self.m * (q_t + self.dt * 0.5 * kappa[0, 0])
        
        kappa[2, 0] = v_t + self.dt * 0.5 * kappa[1, 1]
        kappa[2, 1] = - self.k / self.m * (q_t + self.dt * 0.5 * kappa[1, 0])
        
        kappa[3, 0] = v_t + self.dt * kappa[2, 1]
        kappa[3, 1] = - self.k / self.m * (q_t + self.dt * kappa[2, 0])
        
        self.trajectory_q.append(q_t + self.dt / 6 * np.dot(kappa[:, 0], weights))
        self.trajectory_v.append(v_t + self.dt / 6 * np.dot(kappa[:, 1], weights))
# --8<-- [end:rk4]        
rk4 = RK4(mass, stiffness, dt, q0, v0)
rk4.plot(STEPS, "../assets/1d_mass_spring_rk4.html")

# --8<-- [start:be]
class BackwardEuler(TimeIntegration):
    def one_step(self):
        q_t = self.trajectory_q[-1]
        v_t = self.trajectory_v[-1]
        v = v_t - self.dt * self.k / self.m * q_t
        v = v / (1. + self.dt * self.dt * self.k / self.m)
        self.trajectory_v.append(v)
        self.trajectory_q.append(q_t + self.dt * v)
# --8<-- [end:be]
be = BackwardEuler(mass, stiffness, dt, q0, v0)
be.plot(STEPS, "../assets/1d_mass_spring_be.html")


# --8<-- [start:sc]
class Symplectic(TimeIntegration):
    def one_step(self):
        q_t = self.trajectory_q[-1]
        v_t = self.trajectory_v[-1]
        v = v_t - self.dt * self.k / self.m * q_t
        self.trajectory_v.append(v)
        self.trajectory_q.append(q_t + self.dt * v)
# --8<-- [end:sc]       
sc = Symplectic(mass, stiffness, dt, q0, v0)
sc.plot(STEPS, "../assets/1d_mass_spring_sc.html")