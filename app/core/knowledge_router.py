class RouteDecision:

    def __init__(self, use_knowledge, distance, results):

        self.use_knowledge = use_knowledge
        self.distance = distance
        self.results = results


class KnowledgeRouter:

    THRESHOLD = 1.40

    def __init__(self, knowledge):

        self.knowledge = knowledge

    def route(self, message):

        results = self.knowledge.search(message)

        if not results:

            return RouteDecision(
                False,
                None,
                []
            )

        best = results[0]

        distance = best["distance"]

        return RouteDecision(
            distance <= self.THRESHOLD,
            distance,
            results
        )