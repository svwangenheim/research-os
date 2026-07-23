#!/bin/bash
# Post-merge hook: Remind to update the passport and journal

echo "=== SESSION MERGED TO MAIN ==="
echo ""
echo "Remember to run /checkpoint if you haven't — it updates passport.yaml,"
echo "00_admin/process/journal.md, and _brain/projects/<slug>.md."
echo ""

exit 0
