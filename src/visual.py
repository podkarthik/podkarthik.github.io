from manim import *

class BasicQuadratic(Scene):
    def construct(self):
        ax = Axes(
            x_range = [1.5 - 3, 1.5 + 3], y_range = [-1, 2.5], axis_config = {"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label = "x", y_label = "f(x)")

        def f(x):
            return x ** 2 - 3 * x + 2
        graph = ax.plot(f, color = WHITE)

        self.play(Create(ax))
        self.wait(1)
        self.add(labels)
        self.wait(1)
        self.play(Create(graph), run_time = 3)
        self.wait(1)

class PointsQuadratic(Scene):
    def construct(self):
        ax = Axes(
            x_range = [1.5 - 3, 1.5 + 3], y_range = [-1, 2.5], axis_config = {"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label = "x", y_label = "f(x)")

        def f(x):
            return x ** 2 - 3 * x + 2
        graph = ax.plot(f, color = WHITE)

        self.play(Create(ax))
        self.wait()
        self.add(labels)
        self.wait()

        points = [ ]
        for x in np.linspace(0, 1.5 + 3, 10):
            self.play(Create(Dot(ax.coords_to_point(x, f(x)))))
        self.play(Create(graph), run_time = 3)
        self.wait()