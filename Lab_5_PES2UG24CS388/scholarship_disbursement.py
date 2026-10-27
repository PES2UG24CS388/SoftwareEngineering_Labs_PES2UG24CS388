"""Manage scholarship awards and disbursements."""

import logging
import sqlite3

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE awards (
        id INTEGER PRIMARY KEY,
        student TEXT,
        scheme TEXT,
        amount INTEGER,
        disbursed INTEGER DEFAULT 0
    )
    """
)




def grant(student, scheme, amount, audit=None):
    """Create a scholarship award and record its student."""

    if audit is None:
        audit = []

    if not student.strip() or not scheme.strip():
        raise ValueError("Student and scheme cannot be empty.")

    if not isinstance(amount, int) or isinstance(amount, bool) or amount < 0:
        raise ValueError("Amount must be a non-negative integer.")

    conn.execute(
        """
        INSERT INTO awards (student, scheme, amount, disbursed)
        VALUES (?, ?, ?, 0)
        """,
        (student, scheme, amount),
    )

    audit.append(student)
    return audit


def disburse(award_id):
    """Disburse an award only if it exists and is not already disbursed."""

    row = conn.execute(
        "SELECT amount, disbursed FROM awards WHERE id = ?",
        (award_id,),
    ).fetchone()

    if row is None:
        logger.warning("Award ID %s not found.", award_id)
        return None

    if row[1] == 1:
        logger.warning("Award ID %s already disbursed.", award_id)
        return None

    conn.execute(
        "UPDATE awards SET disbursed = 1 WHERE id = ?",
        (award_id,),
    )

    return row[0]


def archive():
    """Log the archive operation."""

    logger.info("Archiving awards")


def by_scheme_count(scheme):
    """Return the number of awards for a scholarship scheme."""

    if scheme is None:
        return 0

    return conn.execute(
        "SELECT COUNT(*) FROM awards WHERE scheme = ?",
        (scheme,),
    ).fetchone()[0]


def main():
    """Run the scholarship disbursement demonstration."""

    grant("Ishaan", "Merit", 50000)
    grant("Divya", "Need-based", 75000)

    print(disburse(1), disburse(9))
    print(by_scheme_count("Merit"))

    total = conn.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM awards WHERE disbursed = 1"
    ).fetchone()[0]

    print(total)
    archive()


if __name__ == "__main__":
    main()



