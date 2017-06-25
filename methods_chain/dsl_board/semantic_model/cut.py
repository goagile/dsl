from dsl_board.semantic_model.base import CompositeBoardElement
from dsl_board.semantic_model.swimlane import SwimLane


class Cut(CompositeBoardElement):
    row_class = SwimLane
