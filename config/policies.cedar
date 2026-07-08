permit (
    principal == Role::"admin",
    action,
    resource
);

permit (
    principal == Role::"content-agent",
    action == Action::"read",
    resource
) when {
    resource.type == "Product" || resource.type == "Metric" || resource.type == "Feature"
};

forbid (
    principal == Role::"content-agent",
    action == Action::"read",
    resource
) when {
    resource.type == "EmailThread"
};

permit (
    principal == Role::"gtm-agent",
    action == Action::"read",
    resource
) when {
    resource.type == "Product" || resource.type == "ICPSegment" || resource.type == "Persona" || resource.type == "Feature" || resource.type == "Metric"
};
