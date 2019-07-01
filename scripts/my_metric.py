#!/usr/bin/env python
import random
from datadog_checks.checks import AgentCheck

class myCheck(AgentCheck):
  def check(self, instance):
    self.gauge('my_metric', random.randint(0, 1000))
