package None;

/* metamodel_version: 1.11.0 */
/* version: 1.1-rc2 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

@Data
@EqualsAndHashCode(callSuper=false)
public class FieldType  {

  private String lengthId;
  private String nonEncodedFieldId;
  private String discriminatorId;
  private String baseCategory;
  private String baseCategoryAbbrName;
  private String unionDataType;
  private List<FieldRuleType> rule;
  private String assign;
  private Annotation annotation;
  private String type;
  private String codeSet;
  private String abbrName;
  private String scenarioId;
  private String id;
  private String name;
  private String scenario;
  private String added;
  private String addedEp;
  private String changeType;
  private String deprecatedEp;
  private String issue;
  private String lastModified;
  private String replaced;
  private String replacedEp;
  private String replacedByField;
  private String supported;
  private String updated;
  private String updatedEp;
  private String deprecated;
  private String minInclusive;
  private String maxInclusive;
  private Integer implLength;
  private Integer implMinLength;
  private Integer implMaxLength;
  private String presence;
  private String value;
  private String rendering;
  private String encoding;


}